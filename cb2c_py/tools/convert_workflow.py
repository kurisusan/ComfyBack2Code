import json
import re
import importlib
import sys
import os
import inspect
import argparse
from typing import Dict, Any, List, Optional

def sanitize_class_name(name: str) -> str:
    """Converts a name into a valid Python class name."""
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    if sanitized and sanitized[0].isdigit():
        sanitized = "_" + sanitized
    return sanitized

# Add the project root to sys.path to enable importing cb2c_py modules
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

def get_output_slot_name(class_name: str, slot_index: int) -> str:
    """
    Gets the name of an output slot by index for a given node class.
    """
    try:
        module = importlib.import_module(f"cb2c_py.nodes.generated.{class_name.lower()}")
        node_class = getattr(module, class_name)
        
        # We need a dummy node instance to access the outputs class instance
        # This is a bit of a hack, but it's necessary because the outputs
        # are defined in the constructor.
        # We can pass dummy values for the constructor arguments.
        # This is still a bit fragile if the constructor has required args without defaults.
        
        # A better way would be to parse the node class file to get the output names.
        # For now, we will stick to introspection.
        
        # Inspect the constructor to get required arguments
        sig = inspect.signature(node_class.__init__)
        dummy_args = {}
        for param_name, param in sig.parameters.items():
            if param_name == 'self':
                continue
            if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD and param.default is inspect.Parameter.empty:
                # This is a required argument without a default value
                # Try to provide a dummy value based on type hint, or None as a fallback
                if param.annotation is str:
                    dummy_args[param_name] = ""
                elif param.annotation is int:
                    dummy_args[param_name] = 0
                elif param.annotation is float:
                    dummy_args[param_name] = 0.0
                elif param.annotation is bool:
                    dummy_args[param_name] = False
                else:
                    dummy_args[param_name] = None # Fallback for other types
        
        dummy_node = node_class(**dummy_args)
        output_slots = dummy_node.outputs
        
        # The slots are stored in a dict, but we need to access them by order.
        # The order of attributes is preserved in Python 3.7+.
        slot_names = list(vars(output_slots).keys())
        
        if slot_index < len(slot_names):
            return slot_names[slot_index]

    except (ImportError, AttributeError, TypeError) as e:
        print(f"Warning: Could not inspect class {class_name}: {e}")

    return f"outputs[{slot_index}] # Fallback"


def build_python_script(workflow_json: Dict[str, Any], script_name: str, workflow_filename: str, discard_notes: bool = False) -> Optional[str]:
    """
    Generates a Python script from a ComfyUI workflow JSON, separating constructor args from other properties.
    """
    nodes_by_id: Dict[str, Any] = {str(node["id"]): node for node in workflow_json["nodes"]}

    # Pr-check for missing node modules
    for node_data in nodes_by_id.values():
        class_type = node_data["type"]
        if class_type == 'MarkdownNote':
            continue
        py_class_name = sanitize_class_name(class_type)
        try:
            importlib.import_module(f"cb2c_py.nodes.generated.{py_class_name.lower()}")
        except ImportError:
            print(f"Warning: Workflow from '{workflow_filename}' could not be processed due to missing node '{class_type}'. Please try adding the missing node to custom-nodes.txt, then rebuild ComfyUI and regenerate the nodes.")
            return None

    node_vars: Dict[str, str] = {
        node_id: f"{sanitize_class_name(data['type']).lower()}_{node_id}"
        for node_id, data in nodes_by_id.items()
    }

    imports = {"from cb2c_py.lib.workflow import Workflow", "import random"}
    body = [
        f'def {script_name}():',
        '    """',
        f'    This function was auto-generated from a ComfyUI workflow ({workflow_filename}).',
        '    """',
        '    wf = Workflow()',
        ''
    ]

    # Topological sort to determine execution order
    adj: Dict[str, List[str]] = {node_id: [] for node_id in nodes_by_id}
    in_degree: Dict[str, int] = {node_id: 0 for node_id in nodes_by_id}
    for link in workflow_json.get("links", []):
        from_node_id, to_node_id = str(link[1]), str(link[3])
        if from_node_id in adj and to_node_id in in_degree:
            adj[from_node_id].append(to_node_id)
            in_degree[to_node_id] += 1

    queue = [node_id for node_id in nodes_by_id if in_degree[node_id] == 0]
    sorted_node_ids = []
    while queue:
        node_id = queue.pop(0)
        sorted_node_ids.append(node_id)
        for neighbor_id in adj.get(node_id, []):
            in_degree[neighbor_id] -= 1
            if in_degree[neighbor_id] == 0:
                queue.append(neighbor_id)
    
    if len(sorted_node_ids) < len(nodes_by_id):
        print("Warning: Cycle detected or disconnected graph. Appending remaining nodes.")
        sorted_node_ids.extend(node_id for node_id in nodes_by_id if node_id not in sorted_node_ids)

    # Process nodes in sorted order
    for node_id in sorted_node_ids:
        node_data = nodes_by_id[node_id]
        class_type = node_data["type"]
        var_name = node_vars[node_id]

        if class_type == 'MarkdownNote':
            if not discard_notes and (note_text := (node_data.get("widgets_values") or [""])[0]):
                body.extend([f"    # Note from {class_type} (ID: {node_id}):", f"    # {note_text.replace(__import__('os').linesep, ' ')}", ""])
            continue

        py_class_name = sanitize_class_name(class_type)
        try:
            module = importlib.import_module(f"cb2c_py.nodes.generated.{py_class_name.lower()}")
            node_class = getattr(module, py_class_name)
            imports.add(f"from cb2c_py.nodes.generated import {py_class_name}")
        except (ImportError, AttributeError) as e:
            print(f"Error importing node class {py_class_name}: {e}")
            continue

        # Separate constructor args from other properties
        sig = inspect.signature(node_class.__init__)
        constructor_params = {p.name for p in sig.parameters.values() if p.name != 'self'}
        
        all_params = {}
        # Linked inputs
        for inp in node_data.get("inputs", []):
            if (link_id := inp.get("link")) is not None:
                link = next((l for l in workflow_json["links"] if l[0] == link_id), None)
                if link:
                    from_id, from_slot = str(link[1]), link[2]
                    from_var = node_vars[from_id]
                    from_class = sanitize_class_name(nodes_by_id[from_id]["type"])
                    slot_name = get_output_slot_name(from_class, from_slot)
                    all_params[inp["name"]] = f"{from_var}.outputs.{slot_name}"

        # Widget values
        widget_inputs = [inp["name"] for inp in node_data.get("inputs", []) if "widget" in inp]
        for i, value in enumerate(node_data.get("widgets_values", [])):
            if i < len(widget_inputs):
                all_params[widget_inputs[i]] = repr(value)

        constructor_args = {k: v for k, v in all_params.items() if k in constructor_params}
        property_settings = {k: v for k, v in all_params.items() if k not in constructor_params}

        # Build the lines of code for this node
        body.append(f"    # Node: {class_type} (ID: {node_id})")
        constructor_args_str = ', '.join(f"{k}={v}" for k, v in constructor_args.items())
        body.append(f"    {var_name} = {py_class_name}({constructor_args_str})")
        
        for prop, value in property_settings.items():
            body.append(f"    {var_name}.{prop} = {value}")
            
        body.append(f"    wf.add_node({var_name})")
        body.append("")

    script_content = "\n".join(sorted(list(imports))) + "\n\n" + "\n".join(body) + "\n    return wf\n"

    main_block = [
        '',
        'if __name__ == "__main__":',
        '    # Create the workflow',
        f'    workflow = {script_name}()',
        '',
        '    # Run the workflow',
        '    workflow.run()',
        ''
    ]
    script_content += "\n".join(main_block)
    return script_content

def main():
    parser = argparse.ArgumentParser(description="Convert all ComfyUI JSON workflows from 'json-workflows' directory to Python scripts.")
    
    default_output_dir = os.path.join(project_root, "user", "workflows")
    
    parser.add_argument("-o", "--output", 
                        help=f"The path to save the generated Python scripts. Defaults to {default_output_dir}", 
                        default=default_output_dir)
    
    parser.add_argument("--discard-notes", 
                        action='store_true',
                        help="If set, all MarkdownNote nodes will be completely ignored and not even added as comments.")

    args = parser.parse_args()

    output_dir = args.output
    json_workflows_dir = os.path.join(project_root, "json-workflows")

    if not os.path.isdir(json_workflows_dir):
        print(f"Input directory not found: {json_workflows_dir}")
        print(f"Creating directory {json_workflows_dir}. Please add your JSON workflows there and run again.")
        os.makedirs(json_workflows_dir)
        return

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(json_workflows_dir):
        if filename.endswith(".json"):
            json_path = os.path.join(json_workflows_dir, filename)
            
            # Sanitize filename to be a valid python module name
            py_filename_base = sanitize_class_name(filename.replace(".json", "")).lower()
            py_filename = py_filename_base + ".py"
            output_path = os.path.join(output_dir, py_filename)
            
            print(f"Processing {json_path} -> {output_path}")

            try:
                with open(json_path, 'r') as f:
                    workflow_data = json.load(f)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Warning: Could not read or parse {json_path}: {e}")
                continue

            if "prompt" in workflow_data:
                workflow_json = workflow_data["prompt"]
            else:
                workflow_json = workflow_data

            script_name = py_filename_base

            python_script = build_python_script(workflow_json, script_name, filename, discard_notes=args.discard_notes)
            
            if python_script:
                try:
                    with open(output_path, "w") as f:
                        f.write(python_script)
                    print(f"Successfully converted workflow to {output_path}")
                except IOError as e:
                    print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
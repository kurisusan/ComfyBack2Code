import json
import re
import textwrap
import argparse
import requests
import importlib
from typing import Dict, Any, List, Tuple
from urllib.parse import urlparse

def is_url(url: str) -> bool:
    """Check if a string is a valid URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def sanitize_class_name(name: str) -> str:
    """Converts a name into a valid Python class name."""
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    if sanitized and sanitized[0].isdigit():
        sanitized = "_" + sanitized
    return sanitized

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
        
        # Let's assume the node can be instantiated without arguments for introspection.
        # This is a major assumption.
        dummy_node = node_class()
        output_slots = dummy_node.outputs
        
        # The slots are stored in a dict, but we need to access them by order.
        # The order of attributes is preserved in Python 3.7+.
        slot_names = list(vars(output_slots).keys())
        
        if slot_index < len(slot_names):
            return slot_names[slot_index]

    except (ImportError, AttributeError, TypeError) as e:
        print(f"Warning: Could not inspect class {class_name}: {e}")

    return f"outputs[{slot_index}] # Fallback"


def build_python_script(workflow_json: Dict[str, Any], script_name: str) -> str:
    """
    Generates a Python script from a ComfyUI workflow JSON.
    """
    nodes_by_id: Dict[str, Any] = {str(node["id"]): node for node in workflow_json["nodes"]}

    node_vars: Dict[str, str] = {}
    
    for node_id, node_data in nodes_by_id.items():
        class_type = node_data["type"] # Use "type" for class_type
        py_class_name = sanitize_class_name(class_type)
        node_vars[node_id] = f"{py_class_name.lower()}_{node_id}"

    imports = set(["from cb2c_py.lib.workflow import Workflow"])
    
    body = []
    body.append(f'def {script_name}():')
    body.append('    """')
    body.append('    This function was auto-generated from a ComfyUI workflow.')
    body.append('    """')
    body.append('    wf = Workflow()')
    body.append('')

    for node_id, node_data in sorted(nodes_by_id.items(), key=lambda item: int(item[0])):
        class_type = node_data["type"] # Use "type" for class_type
        py_class_name = sanitize_class_name(class_type)
        var_name = node_vars[node_id]
        
        imports.add(f"from cb2c_py.nodes.generated import {py_class_name}")

        inputs_data = node_data.get("inputs", [])
        widgets_values = node_data.get("widgets_values", [])
        args = []
        widget_idx = 0

        for input_item in inputs_data:
            input_name = input_item["name"]
            if "link" in input_item and input_item["link"] is not None:
                # This input is linked to another node's output
                link_id = input_item["link"]
                # Find the link in the workflow_json["links"]
                # A link looks like: [52, 31, 0, 8, 0, "LATENT"]
                # [link_id, from_node_id, from_slot_index, to_node_id, to_slot_index, type]
                
                # We need to find the link that has this link_id as its first element
                found_link = None
                for link in workflow_json["links"]:
                    if link[0] == link_id:
                        found_link = link
                        break
                
                if found_link:
                    from_node_id = str(found_link[1])
                    from_slot_index = found_link[2]
                    
                    from_var_name = node_vars[from_node_id]
                    from_node_data = nodes_by_id[from_node_id]
                    from_class_type = from_node_data["type"]
                    from_py_class_name = sanitize_class_name(from_class_type)

                    output_slot_name = get_output_slot_name(from_py_class_name, from_slot_index)
                    args.append(f'{input_name}={from_var_name}.outputs.{output_slot_name}')
                else:
                    args.append(f'{input_name}=None # Link not found for {link_id}')

            elif "widget" in input_item:
                # This input is a widget with a direct value
                if widget_idx < len(widgets_values):
                    value = widgets_values[widget_idx]
                    args.append(f'{input_name}={repr(value)}')
                    widget_idx += 1
                else:
                    args.append(f'{input_name}=None # Widget value not found')
            else:
                # Fallback for other types of inputs (e.g., direct values not from widgets)
                # This part might need further refinement based on actual JSON structure
                args.append(f'{input_name}=None # Unhandled input type')
        
        # Handle any remaining widgets_values that might not be directly mapped to inputs
        # (e.g., if some inputs are optional or dynamically added)
        while widget_idx < len(widgets_values):
            # This is a heuristic, assuming remaining widget values are for unnamed inputs
            # or inputs that don't have a direct 'name' in the 'inputs' list.
            # This might need more specific logic based on ComfyUI's internal structure.
            # For now, we'll just add them as positional arguments if possible, or skip.
            # This part is highly dependent on how ComfyUI maps widgets to inputs.
            # For now, we'll assume all relevant inputs are in the 'inputs' list.
            widget_idx += 1 # Just consume the value to avoid infinite loop if not handled
        
        body.append(f"    # Node: {class_type} (ID: {node_id})")
        body.append(f"    {var_name} = wf.add_node({py_class_name}({', '.join(args)}))")
        body.append("")

    script_content = "\n".join(sorted(list(imports)))
    script_content += "\n\n"
    script_content += "\n".join(body)
    script_content += "\n    return wf\n"

    return script_content

def main():
    parser = argparse.ArgumentParser(description="Convert a ComfyUI JSON workflow from a URL or Path to a Python script.")
    parser.add_argument("path", help="The Path (or URL) to the JSON workflow file.")
    parser.add_argument("-o", "--output", help="The path to save the generated Python script.", required=True)

    args = parser.parse_args()

    # Check if the path is a URL
    if is_url(args.path):
        try:
            response = requests.get(args.path)
            response.raise_for_status()
            workflow_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")
            return
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the response.")
            return
    else:
        # Treat it as a local file path
        try:
            with open(args.path, 'r') as f:
                workflow_data = json.load(f)
        except IOError as e:
            print(f"Error reading file: {e}")
            return

    if "prompt" in workflow_data:
        workflow_json = workflow_data["prompt"]
    else:
        workflow_json = workflow_data

    script_name = "build_workflow"
    if args.output:
        script_name = re.sub(r'[^a-zA-Z0-9_]', '_', args.output.split('/')[-1].replace('.py', ''))

    python_script = build_python_script(workflow_json, script_name)
    
    try:
        with open(args.output, "w") as f:
            f.write(python_script)
        print(f"Successfully converted workflow to {args.output}")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()

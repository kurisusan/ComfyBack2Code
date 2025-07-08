import json
from typing import Callable, Optional, Dict, Any, TypeAlias
from cb2c_py.nodes.base_node import Node, Slot
from cb2c_py.lib.workflow_runner import WorkflowRunner

ProgressCallback: TypeAlias = Optional[Callable[[Dict[str, Any]], None]]


class Workflow:
    """
    A class to build and manage a ComfyUI workflow graph.
    """

    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.node_to_id: Dict[Node, int] = {}
        self._next_id = 1
        self.runner = WorkflowRunner()

    def add_node(self, node_instance: Node) -> Node:
        """
        Adds a node to the workflow and returns the node instance.
        """
        node_id = self._next_id
        self.nodes[node_id] = node_instance
        self.node_to_id[node_instance] = node_id
        node_instance.id = node_id
        self._next_id += 1
        return node_instance

    def build_workflow_json(self, indent=4) -> str:
        """
        Builds the ComfyUI-compatible JSON representation of the workflow.
        """
        workflow_data = {}
        for node_id, node_instance in self.nodes.items():
            # Process input values to handle Slot connections
            processed_inputs = {}
            for name, value in node_instance.input_values.items():
                if isinstance(value, Slot):
                    # This is a connection from another node
                    source_node_id = self.node_to_id[value._node]
                    source_output_names = [s._name for s in vars(value._node.outputs).values()]
                    source_slot_index = source_output_names.index(value._name)
                    processed_inputs[name] = [str(source_node_id), source_slot_index]
                else:
                    # This is a literal value
                    processed_inputs[name] = value

            workflow_data[str(node_id)] = {
                "inputs": processed_inputs,
                "class_type": node_instance._original_name,
            }

        # The final structure for the API is a dictionary containing the nodes
        api_format = {"prompt": workflow_data}

        return json.dumps(api_format, indent=indent)

    def run(self, progress_callback: ProgressCallback = None):
        """
        Executes the workflow using the WorkflowRunner.
        """
        workflow_json = self.build_workflow_json()
        # print(f"Workflow data: {workflow_json}") # Uncomment for debugging
        self.runner.run_workflow(workflow_json, progress_callback)

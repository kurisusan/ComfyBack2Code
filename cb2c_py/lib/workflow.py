
import json
from .workflow_runner import WorkflowRunner

class Workflow:
    """
    A class to build and manage a ComfyUI workflow graph.
    """
    def __init__(self):
        self.nodes = {}
        self.node_to_id = {}
        self.links = []
        self._next_id = 1
        self.runner = WorkflowRunner()

    def add_node(self, node_instance):
        """
        Adds a node to the workflow and returns the node instance.

        Args:
            node_instance: An instance of a generated node class.

        Returns:
            The node instance passed in, to allow for chaining or easy variable assignment.
        """
        node_id = self._next_id
        self.nodes[node_id] = node_instance
        self.node_to_id[node_instance] = node_id
        self._next_id += 1
        return node_instance

    def connect(self, from_slot, to_slot):
        """
        Connects the output of one node to the input of another.

        Args:
            from_slot (Slot): The output slot of the source node.
            to_slot (Slot): The input slot of the target node.
        """
        from_node_id = self.node_to_id[from_slot.node]
        to_node_id = self.node_to_id[to_slot.node]
        
        link_info = [from_node_id, from_slot.name, to_node_id, to_slot.name]
        self.links.append(link_info)

    def build_workflow_json(self, indent=4):
        """
        Builds the ComfyUI-compatible JSON representation of the workflow.

        Returns:
            str: A JSON string representing the workflow.
        """
        workflow_data = {}
        for node_id, node_instance in self.nodes.items():
            # Get the output slot names for the node class
            output_names = node_instance.get_outputs()

            workflow_data[str(node_id)] = {
                "inputs": node_instance.input_values,
                "class_type": node_instance.original_name,
                "_meta": {
                    "title": node_instance.original_name
                }
            }

        for from_node_id, from_output_slot, to_node_id, to_input_slot in self.links:
            from_node_instance = self.nodes[from_node_id]
            from_output_names = from_node_instance.get_outputs()
            from_slot_index = from_output_slot if isinstance(from_output_slot, int) else from_output_names.index(from_output_slot)
        
            to_input_name = to_input_slot if isinstance(to_input_slot, str) else list(self.nodes[to_node_id].get_inputs().keys())[to_input_slot]
            workflow_data[str(to_node_id)]["inputs"][to_input_name] = [str(from_node_id), from_slot_index]
    

        # Process links
        final_links = []
        link_id = 1
        for from_node_id, from_output_slot, to_node_id, to_input_slot in self.links:
            from_node_instance = self.nodes[from_node_id]
            to_node_instance = self.nodes[to_node_id]

            # Resolve output slot index
            from_output_names = from_node_instance.get_outputs()
            from_slot_index = from_output_slot if isinstance(from_output_slot, int) else from_output_names.index(from_output_slot)
            
            # Resolve output type
            output_type = from_output_names[from_slot_index]

            # Resolve input slot index
            to_input_info = to_node_instance.get_inputs()
            to_input_names = list(to_input_info.keys())
            to_slot_index = to_input_slot if isinstance(to_input_slot, int) else to_input_names.index(to_input_slot)

            final_links.append([
                link_id,
                from_node_id,
                from_slot_index,
                to_node_id,
                to_slot_index,
                output_type
            ])
            link_id += 1
        
        # The final structure for the API is a dictionary containing the nodes
        api_format = {"prompt": workflow_data}

        return json.dumps(api_format, indent=indent)

    def run(self):
        """
        Executes the workflow using the WorkflowRunner.
        """
        # print(f"Workflow data: {self.build_workflow_json()}")
        
        self.runner.run_workflow(self.build_workflow_json())


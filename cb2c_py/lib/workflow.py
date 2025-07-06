
import json
import websocket
import uuid
import urllib.request
import urllib.parse
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get ComfyUI server address from environment variable or use default
DEFAULT_COMFYUI_API_URL = "localhost:8188"
COMFYUI_SERVER_ADDRESS = os.getenv("COMFYUI_API_URL", DEFAULT_COMFYUI_API_URL)

class Workflow:
    """
    A class to build and manage a ComfyUI workflow graph.
    """
    def __init__(self):
        self.nodes = {}
        self.node_to_id = {}
        self.links = []
        self._next_id = 1

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
        
        # The final structure for the API is a dictionary containing the nodes and links
        api_format = {"prompt": workflow_data, "extra_data": {"extra_pnginfo": {"workflow": {"nodes": workflow_data, "links": final_links}}}}

        return json.dumps(api_format, indent=indent)

    def run(self):
        """
        Executes the workflow and saves the output files.
        """
        client_id = str(uuid.uuid4())
        
        # Connect to the websocket
        ws = websocket.WebSocket()
        ws.connect(f"ws://{COMFYUI_SERVER_ADDRESS}/ws?clientId={client_id}")

        print("Executing workflow...")
        files = self._get_outputs(ws, json.loads(self.build_workflow_json()), client_id)

        # Create an 'outputs' directory if it doesn't exist
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)

        # Save the output files
        for file_data, filename in files:
            output_path = output_dir / filename
            with open(output_path, "wb") as f:
                f.write(file_data)
            print(f"File saved to {output_path}")

        ws.close()

    def _queue_prompt(self, prompt, client_id):
        """
        Queues a prompt on the ComfyUI server.
        """
        p = {"prompt": prompt, "client_id": client_id}
        data = json.dumps(p).encode('utf-8')
        req = urllib.request.Request(f"http://{COMFYUI_SERVER_ADDRESS}/prompt", data=data)
        return json.loads(urllib.request.urlopen(req).read())

    def _get_file(self, filename, subfolder, folder_type):
        """
        Gets a file from the ComfyUI server.
        """
        data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
        url_values = urllib.parse.urlencode(data)
        with urllib.request.urlopen(f"http://{COMFYUI_SERVER_ADDRESS}/view?{url_values}") as response:
            return response.read()

    def _get_history(self, prompt_id):
        """
        Gets the execution history for a given prompt ID.
        """
        with urllib.request.urlopen(f"http://{COMFYUI_SERVER_ADDRESS}/history/{prompt_id}") as response:
            return json.loads(response.read())

    def _get_outputs(self, ws, prompt, client_id):
        """
        Executes a prompt and retrieves the output files.
        """
        prompt_id = self._queue_prompt(prompt, client_id)['prompt_id']
        output_files = {}
        
        while True:
            out = ws.recv()
            if isinstance(out, str):
                message = json.loads(out)
                if message['type'] == 'executing':
                    data = message['data']
                    if data['node'] is None and data['prompt_id'] == prompt_id:
                        break  # Execution is done
            else:
                continue # Previews are binary data

        history = self._get_history(prompt_id)[prompt_id]
        for o in history['outputs']:
            for node_id in history['outputs']:
                node_output = history['outputs'][node_id]
                if 'files' in node_output:
                    files_output = []
                    for file in node_output['files']:
                        file_data = self._get_file(file['filename'], file['subfolder'], file['type'])
                        files_output.append((file_data, file['filename']))
                    output_files[node_id] = files_output
                if 'images' in node_output:
                    images_output = []
                    for image in node_output['images']:
                        image_data = self._get_file(image['filename'], image['subfolder'], image['type'])
                        images_output.append((image_data, image['filename']))
                    output_files[node_id] = images_output
        
        for node_id in output_files:
            for file_data, filename in output_files[node_id]:
                yield file_data, filename


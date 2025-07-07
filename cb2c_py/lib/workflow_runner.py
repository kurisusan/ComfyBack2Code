
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
DEFAULT_COMFYUI_SERVER_ADDRESS = "localhost:8188"
COMFYUI_SERVER_ADDRESS = os.getenv("COMFYUI_SERVER_ADDRESS", DEFAULT_COMFYUI_SERVER_ADDRESS)

class WorkflowRunner:
    """
    A class to execute ComfyUI workflows via its API.
    """
    def __init__(self, comfyui_server_address=None):
        self.comfyui_server_address = comfyui_server_address or COMFYUI_SERVER_ADDRESS

    def run_workflow(self, workflow_json):
        """
        Executes the workflow and saves the output files.
        """
        client_id = str(uuid.uuid4())
        
        # Connect to the websocket
        ws = websocket.WebSocket()
        ws.connect(f"ws://{self.comfyui_server_address}/ws?clientId={client_id}")

        print("Executing workflow...")
        files = self._get_outputs(ws, json.loads(workflow_json), client_id)

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
        # Le prompt doit être juste le dictionnaire des nodes, pas le format API complet
        workflow_data = prompt.get("prompt", prompt)  # Extrait juste la partie "prompt"
        
        p = {"prompt": workflow_data, "client_id": client_id}
        data = json.dumps(p).encode('utf-8')
        
        req = urllib.request.Request(f"http://{self.comfyui_server_address}/prompt", data=data)
        req.add_header('Content-Type', 'application/json')
        
        try:
            response = urllib.request.urlopen(req)
            return json.loads(response.read())
        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            print(f"Response: {e.read().decode()}")
            raise

    def _get_file(self, filename, subfolder, folder_type):
        """
        Gets a file from the ComfyUI server.
        """
        data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
        url_values = urllib.parse.urlencode(data)
        with urllib.request.urlopen(f"http://{self.comfyui_server_address}/view?{url_values}") as response:
            return response.read()

    def _get_history(self, prompt_id):
        """
        Gets the execution history for a given prompt ID.
        """
        with urllib.request.urlopen(f"http://{self.comfyui_server_address}/history/{prompt_id}") as response:
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

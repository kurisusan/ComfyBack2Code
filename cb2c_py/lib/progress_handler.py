from typing import Dict, Any, Optional
from tqdm import tqdm

class ComfyUIProgressHandler:
    """
    A callback handler for ComfyUI workflow progress, using tqdm for visualization.
    """
    def __init__(self, name: Optional[str] = None):
        self.pbar = None
        self.name = name if name else "Workflow Progress"

    def __call__(self, message: Dict[str, Any]):
        """
        Processes progress messages from ComfyUI.
        """
        if message['type'] == 'progress':
            data = message['data']
            if self.pbar is None:
                self.pbar = tqdm(total=data['max'], desc=self.name, unit="step")
            self.pbar.update(data['value'] - self.pbar.n)
        elif message['type'] == 'executing':
            data = message['data']
            if data['node'] is not None:
                if self.pbar:
                    self.pbar.set_description(f"{self.name} (Node: {data['node']})")
                else:
                    print(f"Executing node: {data['node']}")
            else:
                if self.pbar:
                    self.pbar.close()
                    self.pbar = None
                print("Workflow execution started or finished.")
        elif message['type'] == 'status':
            data = message['data']
            exec_info = data.get('exec_info')
            if exec_info and exec_info.get('queue_remaining') == 0 and self.pbar:
                self.pbar.close()
                self.pbar = None
            # print(f"Status: {data.get('exec_info')}") # Uncomment for more detailed status
        # else:
            # print(f"Received message: {message['type']}") # Uncomment to see all message types

from typing import Dict, Any, Optional
from tqdm import tqdm


class ComfyUIProgressHandler:
    """
    A callback handler for ComfyUI workflow progress, using tqdm for visualization.
    Each node with progress will have its own progress bar.
    """

    def __init__(self, name: Optional[str] = None):
        self.pbar = None
        if name is not None:
            self.name = name
        else:
            self.name = "Workflow Progress"
        self.current_node_id = None

    def __call__(self, message: Dict[str, Any]):
        """
        Processes progress messages from ComfyUI.
        """
        if message["type"] == "progress":
            data = message["data"]
            if self.pbar is None:
                desc = (
                    f"{self.name} (Node: {self.current_node_id})"
                    if self.current_node_id
                    else self.name
                )
                self.pbar = tqdm(total=data["max"], desc=desc, unit="step")

            current_value = data["value"]
            if current_value > self.pbar.n:
                self.pbar.update(current_value - self.pbar.n)
        elif message["type"] == "executing":
            data = message["data"]
            if data["node"] is not None:
                if self.pbar:
                    # If a progress bar is active, it means a new node is starting.
                    # We complete and close the old one.
                    if self.pbar.n < self.pbar.total:
                        self.pbar.update(self.pbar.total - self.pbar.n)
                    self.pbar.close()
                    self.pbar = None
                self.current_node_id = data["node"]
            else:
                if self.pbar:
                    self.pbar.close()
                    self.pbar = None
                self.current_node_id = None
                print("Workflow execution started or finished.")
        elif message["type"] == "status":
            data = message["data"]
            exec_info = data.get("exec_info")
            if exec_info and exec_info.get("queue_remaining") == 0 and self.pbar:
                self.pbar.close()
                self.pbar = None
            # print(f"Status: {data.get('exec_info')}") # Uncomment for more detailed status
        # else:
        # print(f"Received message: {message['type']}") # Uncomment to see all message types

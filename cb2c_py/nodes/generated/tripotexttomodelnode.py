
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for TripoTextToModelNode
class TripoTextToModelNodeInputs(InputSlots):
    prompt: Slot[str]
    def __init__(self, node: "Node"):
        self.prompt = Slot[str](node, "prompt", 'STRING')

class TripoTextToModelNodeOutputs(OutputSlots):
    model_file: Slot[str]
    model_task_id: Slot[Any]
    def __init__(self, node: "Node"):
        self.model_file = Slot[str](node, "model_file", 'STRING')
        self.model_task_id = Slot[Any](node, "model task_id", 'MODEL_TASK_ID')

class TripoTextToModelNode(Node[TripoTextToModelNodeInputs, TripoTextToModelNodeOutputs]):
    """
    Original name: TripoTextToModelNode
    Category: api node/3d/Tripo
    

    Inputs:
        - prompt (str)

    Outputs:
        - model_file (str)
        - model_task_id (Any)
    """
    _original_name: str = 'TripoTextToModelNode'

    def __init__(self, prompt: str):
        super().__init__(**{"prompt": prompt})
        self.inputs = TripoTextToModelNodeInputs(self)
        self.outputs = TripoTextToModelNodeOutputs(self)

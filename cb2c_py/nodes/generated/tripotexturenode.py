
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for TripoTextureNode
class TripoTextureNodeInputs(InputSlots):
    model_task_id: Slot[Any]
    def __init__(self, node: "Node"):
        self.model_task_id = Slot[Any](node, "model_task_id", 'MODEL_TASK_ID')

class TripoTextureNodeOutputs(OutputSlots):
    model_file: Slot[str]
    model_task_id: Slot[Any]
    def __init__(self, node: "Node"):
        self.model_file = Slot[str](node, "model_file", 'STRING')
        self.model_task_id = Slot[Any](node, "model task_id", 'MODEL_TASK_ID')

class TripoTextureNode(Node[TripoTextureNodeInputs, TripoTextureNodeOutputs]):
    """
    Original name: TripoTextureNode
    Category: api node/3d/Tripo
    

    Inputs:
        - model_task_id (Any)

    Outputs:
        - model_file (str)
        - model_task_id (Any)
    """
    _original_name: str = 'TripoTextureNode'

    def __init__(self, model_task_id: Slot[Any]):
        super().__init__(**{"model_task_id": model_task_id})
        self.inputs = TripoTextureNodeInputs(self)
        self.outputs = TripoTextureNodeOutputs(self)

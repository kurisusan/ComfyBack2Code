
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for TripoRetargetNode
class TripoRetargetNodeInputs(InputSlots):
    original_model_task_id: Slot[Any]
    animation: Slot[str]
    def __init__(self, node: "Node"):
        self.original_model_task_id = Slot[Any](node, "original_model_task_id", 'RIG_TASK_ID')
        self.animation = Slot[str](node, "animation", ['preset:idle', 'preset:walk', 'preset:climb', 'preset:jump', 'preset:slash', 'preset:shoot', 'preset:hurt', 'preset:fall', 'preset:turn'])

class TripoRetargetNodeOutputs(OutputSlots):
    model_file: Slot[str]
    retarget_task_id: Slot[Any]
    def __init__(self, node: "Node"):
        self.model_file = Slot[str](node, "model_file", 'STRING')
        self.retarget_task_id = Slot[Any](node, "retarget task_id", 'RETARGET_TASK_ID')

class TripoRetargetNode(Node[TripoRetargetNodeInputs, TripoRetargetNodeOutputs]):
    """
    Original name: TripoRetargetNode
    Category: api node/3d/Tripo
    

    Inputs:
        - original_model_task_id (Any)
        - animation (str)

    Outputs:
        - model_file (str)
        - retarget_task_id (Any)
    """
    _original_name: str = 'TripoRetargetNode'

    def __init__(self, original_model_task_id: Slot[Any], animation: str):
        super().__init__(**{"original_model_task_id": original_model_task_id, "animation": animation})
        self.inputs = TripoRetargetNodeInputs(self)
        self.outputs = TripoRetargetNodeOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SetHookKeyframes
class SetHookKeyframesInputs(InputSlots):
    hooks: Slot[Any]
    def __init__(self, node: "Node"):
        self.hooks = Slot[Any](node, "hooks", 'HOOKS')

class SetHookKeyframesOutputs(OutputSlots):
    hooks: Slot[Any]
    def __init__(self, node: "Node"):
        self.hooks = Slot[Any](node, "HOOKS", 'HOOKS')

class SetHookKeyframes(Node[SetHookKeyframesInputs, SetHookKeyframesOutputs]):
    """
    Original name: SetHookKeyframes
    Category: advanced/hooks/scheduling
    

    Inputs:
        - hooks (Any)

    Outputs:
        - hooks (Any)
    """
    _original_name: str = 'SetHookKeyframes'

    def __init__(self, hooks: Slot[Any]):
        super().__init__(**{"hooks": hooks})
        self.inputs = SetHookKeyframesInputs(self)
        self.outputs = SetHookKeyframesOutputs(self)

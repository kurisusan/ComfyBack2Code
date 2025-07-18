
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for CombineHooks2
class CombineHooks2Inputs(InputSlots):

    def __init__(self, node: "Node"):
        pass

class CombineHooks2Outputs(OutputSlots):
    hooks: Slot[Any]
    def __init__(self, node: "Node"):
        self.hooks = Slot[Any](node, "HOOKS", 'HOOKS')

class CombineHooks2(Node[CombineHooks2Inputs, CombineHooks2Outputs]):
    """
    Original name: CombineHooks2
    Category: advanced/hooks/combine
    

    Inputs:
        No inputs.

    Outputs:
        - hooks (Any)
    """
    _original_name: str = 'CombineHooks2'

    def __init__(self, ):
        super().__init__(**{})
        self.inputs = CombineHooks2Inputs(self)
        self.outputs = CombineHooks2Outputs(self)

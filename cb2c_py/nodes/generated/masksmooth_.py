
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for MaskSmooth_
class MaskSmooth_Inputs(InputSlots):
    mask: Slot[Image]
    amount: Slot[int]
    def __init__(self, node: "Node"):
        self.mask = Slot[Image](node, "mask", 'MASK')
        self.amount = Slot[int](node, "amount", 'INT')

class MaskSmooth_Outputs(OutputSlots):
    mask: Slot[Image]
    def __init__(self, node: "Node"):
        self.mask = Slot[Image](node, "MASK", 'MASK')

class MaskSmooth_(Node[MaskSmooth_Inputs, MaskSmooth_Outputs]):
    """
    Original name: MaskSmooth+
    Category: essentials/mask
    

    Inputs:
        - mask (Image)
        - amount (int) (default: 0)

    Outputs:
        - mask (Image)
    """
    _original_name: str = 'MaskSmooth+'

    def __init__(self, mask: Slot[Image], amount: int = 0):
        super().__init__(**{"mask": mask, "amount": amount})
        self.inputs = MaskSmooth_Inputs(self)
        self.outputs = MaskSmooth_Outputs(self)

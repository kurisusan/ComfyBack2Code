
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for GrowMask
class GrowMaskInputs(InputSlots):
    mask: Slot[Image]
    expand: Slot[int]
    tapered_corners: Slot[bool]
    def __init__(self, node: "Node"):
        self.mask = Slot[Image](node, "mask", 'MASK')
        self.expand = Slot[int](node, "expand", 'INT')
        self.tapered_corners = Slot[bool](node, "tapered_corners", 'BOOLEAN')

class GrowMaskOutputs(OutputSlots):
    mask: Slot[Image]
    def __init__(self, node: "Node"):
        self.mask = Slot[Image](node, "MASK", 'MASK')

class GrowMask(Node[GrowMaskInputs, GrowMaskOutputs]):
    """
    Original name: GrowMask
    Category: mask
    

    Inputs:
        - mask (Image)
        - expand (int) (default: 0)
        - tapered_corners (bool) (default: True)

    Outputs:
        - mask (Image)
    """
    _original_name: str = 'GrowMask'

    def __init__(self, mask: Slot[Image], expand: int = 0, tapered_corners: bool = True):
        super().__init__(**{"mask": mask, "expand": expand, "tapered_corners": tapered_corners})
        self.inputs = GrowMaskInputs(self)
        self.outputs = GrowMaskOutputs(self)

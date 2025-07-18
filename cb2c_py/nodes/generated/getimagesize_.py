
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for GetImageSize_
class GetImageSize_Inputs(InputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')

class GetImageSize_Outputs(OutputSlots):
    width: Slot[int]
    height: Slot[int]
    count: Slot[int]
    def __init__(self, node: "Node"):
        self.width = Slot[int](node, "width", 'INT')
        self.height = Slot[int](node, "height", 'INT')
        self.count = Slot[int](node, "count", 'INT')

class GetImageSize_(Node[GetImageSize_Inputs, GetImageSize_Outputs]):
    """
    Original name: GetImageSize+
    Category: essentials/image utils
    

    Inputs:
        - image (Image)

    Outputs:
        - width (int)
        - height (int)
        - count (int)
    """
    _original_name: str = 'GetImageSize+'

    def __init__(self, image: Slot[Image]):
        super().__init__(**{"image": image})
        self.inputs = GetImageSize_Inputs(self)
        self.outputs = GetImageSize_Outputs(self)

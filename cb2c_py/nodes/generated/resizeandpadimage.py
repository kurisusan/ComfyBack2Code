
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ResizeAndPadImage
class ResizeAndPadImageInputs(InputSlots):
    image: Slot[Image]
    target_width: Slot[int]
    target_height: Slot[int]
    padding_color: Slot[str]
    interpolation: Slot[str]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.target_width = Slot[int](node, "target_width", 'INT')
        self.target_height = Slot[int](node, "target_height", 'INT')
        self.padding_color = Slot[str](node, "padding_color", ['white', 'black'])
        self.interpolation = Slot[str](node, "interpolation", ['area', 'bicubic', 'nearest-exact', 'bilinear', 'lanczos'])

class ResizeAndPadImageOutputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class ResizeAndPadImage(Node[ResizeAndPadImageInputs, ResizeAndPadImageOutputs]):
    """
    Original name: ResizeAndPadImage
    Category: image/transform
    

    Inputs:
        - image (Image)
        - target_width (int) (default: 512)
        - target_height (int) (default: 512)
        - padding_color (str)
        - interpolation (str)

    Outputs:
        - image (Image)
    """
    _original_name: str = 'ResizeAndPadImage'

    def __init__(self, image: Slot[Image], padding_color: str, interpolation: str, target_width: int = 512, target_height: int = 512):
        super().__init__(**{"image": image, "target_width": target_width, "target_height": target_height, "padding_color": padding_color, "interpolation": interpolation})
        self.inputs = ResizeAndPadImageInputs(self)
        self.outputs = ResizeAndPadImageOutputs(self)

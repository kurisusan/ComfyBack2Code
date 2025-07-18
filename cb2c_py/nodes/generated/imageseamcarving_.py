
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ImageSeamCarving_
class ImageSeamCarving_Inputs(InputSlots):
    image: Slot[Image]
    width: Slot[int]
    height: Slot[int]
    energy: Slot[str]
    order: Slot[str]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.width = Slot[int](node, "width", 'INT')
        self.height = Slot[int](node, "height", 'INT')
        self.energy = Slot[str](node, "energy", ['backward', 'forward'])
        self.order = Slot[str](node, "order", ['width-first', 'height-first'])

class ImageSeamCarving_Outputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class ImageSeamCarving_(Node[ImageSeamCarving_Inputs, ImageSeamCarving_Outputs]):
    """
    Original name: ImageSeamCarving+
    Category: essentials/image manipulation
    

    Inputs:
        - image (Image)
        - width (int) (default: 512)
        - height (int) (default: 512)
        - energy (str)
        - order (str)

    Outputs:
        - image (Image)
    """
    _original_name: str = 'ImageSeamCarving+'

    def __init__(self, image: Slot[Image], energy: str, order: str, width: int = 512, height: int = 512):
        super().__init__(**{"image": image, "width": width, "height": height, "energy": energy, "order": order})
        self.inputs = ImageSeamCarving_Inputs(self)
        self.outputs = ImageSeamCarving_Outputs(self)

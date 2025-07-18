
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for Image_Inset_Crop__rgthree_
class Image_Inset_Crop__rgthree_Inputs(InputSlots):
    image: Slot[Image]
    measurement: Slot[str]
    left: Slot[int]
    right: Slot[int]
    top: Slot[int]
    bottom: Slot[int]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.measurement = Slot[str](node, "measurement", ['Pixels', 'Percentage'])
        self.left = Slot[int](node, "left", 'INT')
        self.right = Slot[int](node, "right", 'INT')
        self.top = Slot[int](node, "top", 'INT')
        self.bottom = Slot[int](node, "bottom", 'INT')

class Image_Inset_Crop__rgthree_Outputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class Image_Inset_Crop__rgthree_(Node[Image_Inset_Crop__rgthree_Inputs, Image_Inset_Crop__rgthree_Outputs]):
    """
    Original name: Image Inset Crop (rgthree)
    Category: rgthree
    

    Inputs:
        - image (Image)
        - measurement (str)
        - left (int) (default: 0)
        - right (int) (default: 0)
        - top (int) (default: 0)
        - bottom (int) (default: 0)

    Outputs:
        - image (Image)
    """
    _original_name: str = 'Image Inset Crop (rgthree)'

    def __init__(self, image: Slot[Image], measurement: str, left: int = 0, right: int = 0, top: int = 0, bottom: int = 0):
        super().__init__(**{"image": image, "measurement": measurement, "left": left, "right": right, "top": top, "bottom": bottom})
        self.inputs = Image_Inset_Crop__rgthree_Inputs(self)
        self.outputs = Image_Inset_Crop__rgthree_Outputs(self)

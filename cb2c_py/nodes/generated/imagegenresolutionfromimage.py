
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ImageGenResolutionFromImage
class ImageGenResolutionFromImageInputs(InputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')

class ImageGenResolutionFromImageOutputs(OutputSlots):
    image_gen_width__int_: Slot[int]
    image_gen_height__int_: Slot[int]
    def __init__(self, node: "Node"):
        self.image_gen_width__int_ = Slot[int](node, "IMAGE_GEN_WIDTH (INT)", 'INT')
        self.image_gen_height__int_ = Slot[int](node, "IMAGE_GEN_HEIGHT (INT)", 'INT')

class ImageGenResolutionFromImage(Node[ImageGenResolutionFromImageInputs, ImageGenResolutionFromImageOutputs]):
    """
    Original name: ImageGenResolutionFromImage
    Category: ControlNet Preprocessors
    

    Inputs:
        - image (Image)

    Outputs:
        - image_gen_width__int_ (int)
        - image_gen_height__int_ (int)
    """
    _original_name: str = 'ImageGenResolutionFromImage'

    def __init__(self, image: Slot[Image]):
        super().__init__(**{"image": image})
        self.inputs = ImageGenResolutionFromImageInputs(self)
        self.outputs = ImageGenResolutionFromImageOutputs(self)

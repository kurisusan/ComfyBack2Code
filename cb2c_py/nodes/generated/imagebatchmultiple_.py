
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ImageBatchMultiple_
class ImageBatchMultiple_Inputs(InputSlots):
    image_1: Slot[Image]
    method: Slot[str]
    def __init__(self, node: "Node"):
        self.image_1 = Slot[Image](node, "image_1", 'IMAGE')
        self.method = Slot[str](node, "method", ['nearest-exact', 'bilinear', 'area', 'bicubic', 'lanczos'])

class ImageBatchMultiple_Outputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class ImageBatchMultiple_(Node[ImageBatchMultiple_Inputs, ImageBatchMultiple_Outputs]):
    """
    Original name: ImageBatchMultiple+
    Category: essentials/image batch
    

    Inputs:
        - image_1 (Image)
        - method (str) (default: 'lanczos')

    Outputs:
        - image (Image)
    """
    _original_name: str = 'ImageBatchMultiple+'

    def __init__(self, image_1: Slot[Image], method: str = 'lanczos'):
        super().__init__(**{"image_1": image_1, "method": method})
        self.inputs = ImageBatchMultiple_Inputs(self)
        self.outputs = ImageBatchMultiple_Outputs(self)

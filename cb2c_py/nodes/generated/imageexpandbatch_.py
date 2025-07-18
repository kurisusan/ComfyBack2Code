
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ImageExpandBatch_
class ImageExpandBatch_Inputs(InputSlots):
    image: Slot[Image]
    size: Slot[int]
    method: Slot[str]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.size = Slot[int](node, "size", 'INT')
        self.method = Slot[str](node, "method", ['expand', 'repeat all', 'repeat first', 'repeat last'])

class ImageExpandBatch_Outputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class ImageExpandBatch_(Node[ImageExpandBatch_Inputs, ImageExpandBatch_Outputs]):
    """
    Original name: ImageExpandBatch+
    Category: essentials/image batch
    

    Inputs:
        - image (Image)
        - size (int) (default: 16)
        - method (str)

    Outputs:
        - image (Image)
    """
    _original_name: str = 'ImageExpandBatch+'

    def __init__(self, image: Slot[Image], method: str, size: int = 16):
        super().__init__(**{"image": image, "size": size, "method": method})
        self.inputs = ImageExpandBatch_Inputs(self)
        self.outputs = ImageExpandBatch_Outputs(self)

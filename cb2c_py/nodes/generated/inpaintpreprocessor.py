
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for InpaintPreprocessor
class InpaintPreprocessorInputs(InputSlots):
    image: Slot[Image]
    mask: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.mask = Slot[Image](node, "mask", 'MASK')

class InpaintPreprocessorOutputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class InpaintPreprocessor(Node[InpaintPreprocessorInputs, InpaintPreprocessorOutputs]):
    """
    Original name: InpaintPreprocessor
    Category: ControlNet Preprocessors/others
    

    Inputs:
        - image (Image)
        - mask (Image)

    Outputs:
        - image (Image)
    """
    _original_name: str = 'InpaintPreprocessor'

    def __init__(self, image: Slot[Image], mask: Slot[Image]):
        super().__init__(**{"image": image, "mask": mask})
        self.inputs = InpaintPreprocessorInputs(self)
        self.outputs = InpaintPreprocessorOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for BinaryPreprocessor
class BinaryPreprocessorInputs(InputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')

class BinaryPreprocessorOutputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class BinaryPreprocessor(Node[BinaryPreprocessorInputs, BinaryPreprocessorOutputs]):
    """
    Original name: BinaryPreprocessor
    Category: ControlNet Preprocessors/Line Extractors
    

    Inputs:
        - image (Image)

    Outputs:
        - image (Image)
    """
    _original_name: str = 'BinaryPreprocessor'

    def __init__(self, image: Slot[Image]):
        super().__init__(**{"image": image})
        self.inputs = BinaryPreprocessorInputs(self)
        self.outputs = BinaryPreprocessorOutputs(self)

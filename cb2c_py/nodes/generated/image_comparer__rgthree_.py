
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for Image_Comparer__rgthree_
class Image_Comparer__rgthree_Inputs(InputSlots):

    def __init__(self, node: "Node"):
        pass

class Image_Comparer__rgthree_Outputs(OutputSlots):

    def __init__(self, node: "Node"):
        pass

class Image_Comparer__rgthree_(Node[Image_Comparer__rgthree_Inputs, Image_Comparer__rgthree_Outputs]):
    """
    Original name: Image Comparer (rgthree)
    Category: rgthree
    Saves the input images to your ComfyUI output directory.

    Inputs:
        No inputs.

    Outputs:
        No outputs.
    """
    _original_name: str = 'Image Comparer (rgthree)'

    def __init__(self, ):
        super().__init__(**{})
        self.inputs = Image_Comparer__rgthree_Inputs(self)
        self.outputs = Image_Comparer__rgthree_Outputs(self)

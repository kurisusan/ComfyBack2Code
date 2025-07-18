
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for LoadImageMask
class LoadImageMaskInputs(InputSlots):
    image: Slot[str]
    channel: Slot[str]
    def __init__(self, node: "Node"):
        self.image = Slot[str](node, "image", ['example.png'])
        self.channel = Slot[str](node, "channel", ['alpha', 'red', 'green', 'blue'])

class LoadImageMaskOutputs(OutputSlots):
    mask: Slot[Image]
    def __init__(self, node: "Node"):
        self.mask = Slot[Image](node, "MASK", 'MASK')

class LoadImageMask(Node[LoadImageMaskInputs, LoadImageMaskOutputs]):
    """
    Original name: LoadImageMask
    Category: mask
    

    Inputs:
        - image (str)
        - channel (str)

    Outputs:
        - mask (Image)
    """
    _original_name: str = 'LoadImageMask'

    def __init__(self, image: str, channel: str):
        super().__init__(**{"image": image, "channel": channel})
        self.inputs = LoadImageMaskInputs(self)
        self.outputs = LoadImageMaskOutputs(self)

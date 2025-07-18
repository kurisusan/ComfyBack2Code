
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for EmptyLTXVLatentVideo
class EmptyLTXVLatentVideoInputs(InputSlots):
    width: Slot[int]
    height: Slot[int]
    length: Slot[int]
    batch_size: Slot[int]
    def __init__(self, node: "Node"):
        self.width = Slot[int](node, "width", 'INT')
        self.height = Slot[int](node, "height", 'INT')
        self.length = Slot[int](node, "length", 'INT')
        self.batch_size = Slot[int](node, "batch_size", 'INT')

class EmptyLTXVLatentVideoOutputs(OutputSlots):
    latent: Slot[Latent]
    def __init__(self, node: "Node"):
        self.latent = Slot[Latent](node, "LATENT", 'LATENT')

class EmptyLTXVLatentVideo(Node[EmptyLTXVLatentVideoInputs, EmptyLTXVLatentVideoOutputs]):
    """
    Original name: EmptyLTXVLatentVideo
    Category: latent/video/ltxv
    

    Inputs:
        - width (int) (default: 768)
        - height (int) (default: 512)
        - length (int) (default: 97)
        - batch_size (int) (default: 1)

    Outputs:
        - latent (Latent)
    """
    _original_name: str = 'EmptyLTXVLatentVideo'

    def __init__(self, width: int = 768, height: int = 512, length: int = 97, batch_size: int = 1):
        super().__init__(**{"width": width, "height": height, "length": length, "batch_size": batch_size})
        self.inputs = EmptyLTXVLatentVideoInputs(self)
        self.outputs = EmptyLTXVLatentVideoOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for CLIPMergeSimple
class CLIPMergeSimpleInputs(InputSlots):
    clip1: Slot[Clip]
    clip2: Slot[Clip]
    ratio: Slot[float]
    def __init__(self, node: "Node"):
        self.clip1 = Slot[Clip](node, "clip1", 'CLIP')
        self.clip2 = Slot[Clip](node, "clip2", 'CLIP')
        self.ratio = Slot[float](node, "ratio", 'FLOAT')

class CLIPMergeSimpleOutputs(OutputSlots):
    clip: Slot[Clip]
    def __init__(self, node: "Node"):
        self.clip = Slot[Clip](node, "CLIP", 'CLIP')

class CLIPMergeSimple(Node[CLIPMergeSimpleInputs, CLIPMergeSimpleOutputs]):
    """
    Original name: CLIPMergeSimple
    Category: advanced/model_merging
    

    Inputs:
        - clip1 (Clip)
        - clip2 (Clip)
        - ratio (float) (default: 1.0)

    Outputs:
        - clip (Clip)
    """
    _original_name: str = 'CLIPMergeSimple'

    def __init__(self, clip1: Slot[Clip], clip2: Slot[Clip], ratio: float = 1.0):
        super().__init__(**{"clip1": clip1, "clip2": clip2, "ratio": ratio})
        self.inputs = CLIPMergeSimpleInputs(self)
        self.outputs = CLIPMergeSimpleOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for CLIPTextEncodeSD3
class CLIPTextEncodeSD3Inputs(InputSlots):
    clip: Slot[Clip]
    clip_l: Slot[str]
    clip_g: Slot[str]
    t5xxl: Slot[str]
    empty_padding: Slot[str]
    def __init__(self, node: "Node"):
        self.clip = Slot[Clip](node, "clip", 'CLIP')
        self.clip_l = Slot[str](node, "clip_l", 'STRING')
        self.clip_g = Slot[str](node, "clip_g", 'STRING')
        self.t5xxl = Slot[str](node, "t5xxl", 'STRING')
        self.empty_padding = Slot[str](node, "empty_padding", ['none', 'empty_prompt'])

class CLIPTextEncodeSD3Outputs(OutputSlots):
    conditioning: Slot[Conditioning]
    def __init__(self, node: "Node"):
        self.conditioning = Slot[Conditioning](node, "CONDITIONING", 'CONDITIONING')

class CLIPTextEncodeSD3(Node[CLIPTextEncodeSD3Inputs, CLIPTextEncodeSD3Outputs]):
    """
    Original name: CLIPTextEncodeSD3
    Category: advanced/conditioning
    

    Inputs:
        - clip (Clip)
        - clip_l (str)
        - clip_g (str)
        - t5xxl (str)
        - empty_padding (str)

    Outputs:
        - conditioning (Conditioning)
    """
    _original_name: str = 'CLIPTextEncodeSD3'

    def __init__(self, clip: Slot[Clip], clip_l: str, clip_g: str, t5xxl: str, empty_padding: str):
        super().__init__(**{"clip": clip, "clip_l": clip_l, "clip_g": clip_g, "t5xxl": t5xxl, "empty_padding": empty_padding})
        self.inputs = CLIPTextEncodeSD3Inputs(self)
        self.outputs = CLIPTextEncodeSD3Outputs(self)

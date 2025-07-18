
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for CLIPTextEncodeHiDream
class CLIPTextEncodeHiDreamInputs(InputSlots):
    clip: Slot[Clip]
    clip_l: Slot[str]
    clip_g: Slot[str]
    t5xxl: Slot[str]
    llama: Slot[str]
    def __init__(self, node: "Node"):
        self.clip = Slot[Clip](node, "clip", 'CLIP')
        self.clip_l = Slot[str](node, "clip_l", 'STRING')
        self.clip_g = Slot[str](node, "clip_g", 'STRING')
        self.t5xxl = Slot[str](node, "t5xxl", 'STRING')
        self.llama = Slot[str](node, "llama", 'STRING')

class CLIPTextEncodeHiDreamOutputs(OutputSlots):
    conditioning: Slot[Conditioning]
    def __init__(self, node: "Node"):
        self.conditioning = Slot[Conditioning](node, "CONDITIONING", 'CONDITIONING')

class CLIPTextEncodeHiDream(Node[CLIPTextEncodeHiDreamInputs, CLIPTextEncodeHiDreamOutputs]):
    """
    Original name: CLIPTextEncodeHiDream
    Category: advanced/conditioning
    

    Inputs:
        - clip (Clip)
        - clip_l (str)
        - clip_g (str)
        - t5xxl (str)
        - llama (str)

    Outputs:
        - conditioning (Conditioning)
    """
    _original_name: str = 'CLIPTextEncodeHiDream'

    def __init__(self, clip: Slot[Clip], clip_l: str, clip_g: str, t5xxl: str, llama: str):
        super().__init__(**{"clip": clip, "clip_l": clip_l, "clip_g": clip_g, "t5xxl": t5xxl, "llama": llama})
        self.inputs = CLIPTextEncodeHiDreamInputs(self)
        self.outputs = CLIPTextEncodeHiDreamOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for WanVideoATI_comfy
class WanVideoATI_comfyInputs(InputSlots):
    model: Slot[Model]
    width: Slot[int]
    height: Slot[int]
    tracks: Slot[str]
    temperature: Slot[float]
    topk: Slot[int]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')
        self.width = Slot[int](node, "width", 'INT')
        self.height = Slot[int](node, "height", 'INT')
        self.tracks = Slot[str](node, "tracks", 'STRING')
        self.temperature = Slot[float](node, "temperature", 'FLOAT')
        self.topk = Slot[int](node, "topk", 'INT')

class WanVideoATI_comfyOutputs(OutputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')

class WanVideoATI_comfy(Node[WanVideoATI_comfyInputs, WanVideoATI_comfyOutputs]):
    """
    Original name: WanVideoATI_comfy
    Category: WanVideoWrapper
    

    Inputs:
        - model (Model)
        - width (int) (default: 832)
          Width of the image to encode
        - height (int) (default: 480)
          Height of the image to encode
        - tracks (str)
        - temperature (float) (default: 220.0)
        - topk (int) (default: 2)

    Outputs:
        - model (Model)
    """
    _original_name: str = 'WanVideoATI_comfy'

    def __init__(self, model: Slot[Model], tracks: str, width: int = 832, height: int = 480, temperature: float = 220.0, topk: int = 2):
        super().__init__(**{"model": model, "width": width, "height": height, "tracks": tracks, "temperature": temperature, "topk": topk})
        self.inputs = WanVideoATI_comfyInputs(self)
        self.outputs = WanVideoATI_comfyOutputs(self)

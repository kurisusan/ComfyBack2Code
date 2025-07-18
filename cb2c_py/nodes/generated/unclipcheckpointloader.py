
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for unCLIPCheckpointLoader
class unCLIPCheckpointLoaderInputs(InputSlots):
    ckpt_name: Slot[str]
    def __init__(self, node: "Node"):
        self.ckpt_name = Slot[str](node, "ckpt_name", ['v1-5-pruned-emaonly.safetensors'])

class unCLIPCheckpointLoaderOutputs(OutputSlots):
    model: Slot[Model]
    clip: Slot[Clip]
    vae: Slot[Vae]
    clip_vision: Slot[Any]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "MODEL", 'MODEL')
        self.clip = Slot[Clip](node, "CLIP", 'CLIP')
        self.vae = Slot[Vae](node, "VAE", 'VAE')
        self.clip_vision = Slot[Any](node, "CLIP_VISION", 'CLIP_VISION')

class unCLIPCheckpointLoader(Node[unCLIPCheckpointLoaderInputs, unCLIPCheckpointLoaderOutputs]):
    """
    Original name: unCLIPCheckpointLoader
    Category: loaders
    

    Inputs:
        - ckpt_name (str)

    Outputs:
        - model (Model)
        - clip (Clip)
        - vae (Vae)
        - clip_vision (Any)
    """
    _original_name: str = 'unCLIPCheckpointLoader'

    def __init__(self, ckpt_name: str):
        super().__init__(**{"ckpt_name": ckpt_name})
        self.inputs = unCLIPCheckpointLoaderInputs(self)
        self.outputs = unCLIPCheckpointLoaderOutputs(self)

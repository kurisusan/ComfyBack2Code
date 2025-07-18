
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for Intrinsic_lora_sampling
class Intrinsic_lora_samplingInputs(InputSlots):
    model: Slot[Model]
    lora_name: Slot[str]
    task: Slot[str]
    text: Slot[str]
    clip: Slot[Clip]
    vae: Slot[Vae]
    per_batch: Slot[int]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')
        self.lora_name = Slot[str](node, "lora_name", ['intrinsic_lora_sd15_albedo.safetensors', 'intrinsic_lora_sd15_depth.safetensors', 'intrinsic_lora_sd15_normal.safetensors', 'intrinsic_lora_sd15_shading.safetensors', 'intrinsic_loras.txt'])
        self.task = Slot[str](node, "task", ['depth map', 'surface normals', 'albedo', 'shading'])
        self.text = Slot[str](node, "text", 'STRING')
        self.clip = Slot[Clip](node, "clip", 'CLIP')
        self.vae = Slot[Vae](node, "vae", 'VAE')
        self.per_batch = Slot[int](node, "per_batch", 'INT')

class Intrinsic_lora_samplingOutputs(OutputSlots):
    image: Slot[Image]
    latent: Slot[Latent]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')
        self.latent = Slot[Latent](node, "LATENT", 'LATENT')

class Intrinsic_lora_sampling(Node[Intrinsic_lora_samplingInputs, Intrinsic_lora_samplingOutputs]):
    """
    Original name: Intrinsic_lora_sampling
    Category: KJNodes
    
Sampler to use the intrinsic loras:  
https://github.com/duxiaodan/intrinsic-lora  
These LoRAs are tiny and thus included  
with this node pack.


    Inputs:
        - model (Model)
        - lora_name (str)
        - task (str) (default: 'depth map')
        - text (str) (default: '')
        - clip (Clip)
        - vae (Vae)
        - per_batch (int) (default: 16)

    Outputs:
        - image (Image)
        - latent (Latent)
    """
    _original_name: str = 'Intrinsic_lora_sampling'

    def __init__(self, model: Slot[Model], lora_name: str, clip: Slot[Clip], vae: Slot[Vae], task: str = 'depth map', text: str = '', per_batch: int = 16):
        super().__init__(**{"model": model, "lora_name": lora_name, "task": task, "text": text, "clip": clip, "vae": vae, "per_batch": per_batch})
        self.inputs = Intrinsic_lora_samplingInputs(self)
        self.outputs = Intrinsic_lora_samplingOutputs(self)

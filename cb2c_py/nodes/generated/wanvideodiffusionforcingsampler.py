
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for WanVideoDiffusionForcingSampler
class WanVideoDiffusionForcingSamplerInputs(InputSlots):
    model: Slot[Any]
    text_embeds: Slot[Any]
    image_embeds: Slot[Any]
    addnoise_condition: Slot[int]
    fps: Slot[float]
    steps: Slot[int]
    cfg: Slot[float]
    shift: Slot[float]
    seed: Slot[int]
    force_offload: Slot[bool]
    scheduler: Slot[str]
    def __init__(self, node: "Node"):
        self.model = Slot[Any](node, "model", 'WANVIDEOMODEL')
        self.text_embeds = Slot[Any](node, "text_embeds", 'WANVIDEOTEXTEMBEDS')
        self.image_embeds = Slot[Any](node, "image_embeds", 'WANVIDIMAGE_EMBEDS')
        self.addnoise_condition = Slot[int](node, "addnoise_condition", 'INT')
        self.fps = Slot[float](node, "fps", 'FLOAT')
        self.steps = Slot[int](node, "steps", 'INT')
        self.cfg = Slot[float](node, "cfg", 'FLOAT')
        self.shift = Slot[float](node, "shift", 'FLOAT')
        self.seed = Slot[int](node, "seed", 'INT')
        self.force_offload = Slot[bool](node, "force_offload", 'BOOLEAN')
        self.scheduler = Slot[str](node, "scheduler", ['unipc', 'unipc/beta', 'euler', 'euler/beta', 'lcm', 'lcm/beta'])

class WanVideoDiffusionForcingSamplerOutputs(OutputSlots):
    samples: Slot[Latent]
    def __init__(self, node: "Node"):
        self.samples = Slot[Latent](node, "samples", 'LATENT')

class WanVideoDiffusionForcingSampler(Node[WanVideoDiffusionForcingSamplerInputs, WanVideoDiffusionForcingSamplerOutputs]):
    """
    Original name: WanVideoDiffusionForcingSampler
    Category: WanVideoWrapper
    

    Inputs:
        - model (Any)
        - text_embeds (Any)
        - image_embeds (Any)
        - addnoise_condition (int) (default: 10)
          Improves consistency in long video generation
        - fps (float) (default: 24.0)
        - steps (int) (default: 30)
        - cfg (float) (default: 6.0)
        - shift (float) (default: 8.0)
        - seed (int) (default: 0)
        - force_offload (bool) (default: True)
          Moves the model to the offload device after sampling
        - scheduler (str) (default: 'unipc')

    Outputs:
        - samples (Latent)
    """
    _original_name: str = 'WanVideoDiffusionForcingSampler'

    def __init__(self, model: Slot[Any], text_embeds: Slot[Any], image_embeds: Slot[Any], addnoise_condition: int = 10, fps: float = 24.0, steps: int = 30, cfg: float = 6.0, shift: float = 8.0, seed: int = 0, force_offload: bool = True, scheduler: str = 'unipc'):
        super().__init__(**{"model": model, "text_embeds": text_embeds, "image_embeds": image_embeds, "addnoise_condition": addnoise_condition, "fps": fps, "steps": steps, "cfg": cfg, "shift": shift, "seed": seed, "force_offload": force_offload, "scheduler": scheduler})
        self.inputs = WanVideoDiffusionForcingSamplerInputs(self)
        self.outputs = WanVideoDiffusionForcingSamplerOutputs(self)

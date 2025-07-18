
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for WanVideoSampler
class WanVideoSamplerInputs(InputSlots):
    model: Slot[Any]
    image_embeds: Slot[Any]
    steps: Slot[int]
    cfg: Slot[float]
    shift: Slot[float]
    seed: Slot[int]
    force_offload: Slot[bool]
    scheduler: Slot[str]
    riflex_freq_index: Slot[int]
    def __init__(self, node: "Node"):
        self.model = Slot[Any](node, "model", 'WANVIDEOMODEL')
        self.image_embeds = Slot[Any](node, "image_embeds", 'WANVIDIMAGE_EMBEDS')
        self.steps = Slot[int](node, "steps", 'INT')
        self.cfg = Slot[float](node, "cfg", 'FLOAT')
        self.shift = Slot[float](node, "shift", 'FLOAT')
        self.seed = Slot[int](node, "seed", 'INT')
        self.force_offload = Slot[bool](node, "force_offload", 'BOOLEAN')
        self.scheduler = Slot[str](node, "scheduler", ['unipc', 'unipc/beta', 'dpm++', 'dpm++/beta', 'dpm++_sde', 'dpm++_sde/beta', 'euler', 'euler/beta', 'euler/accvideo', 'deis', 'lcm', 'lcm/beta', 'flowmatch_causvid', 'flowmatch_distill', 'multitalk'])
        self.riflex_freq_index = Slot[int](node, "riflex_freq_index", 'INT')

class WanVideoSamplerOutputs(OutputSlots):
    samples: Slot[Latent]
    def __init__(self, node: "Node"):
        self.samples = Slot[Latent](node, "samples", 'LATENT')

class WanVideoSampler(Node[WanVideoSamplerInputs, WanVideoSamplerOutputs]):
    """
    Original name: WanVideoSampler
    Category: WanVideoWrapper
    

    Inputs:
        - model (Any)
        - image_embeds (Any)
        - steps (int) (default: 30)
        - cfg (float) (default: 6.0)
        - shift (float) (default: 5.0)
        - seed (int) (default: 0)
        - force_offload (bool) (default: True)
          Moves the model to the offload device after sampling
        - scheduler (str) (default: 'unipc')
        - riflex_freq_index (int) (default: 0)
          Frequency index for RIFLEX, disabled when 0, default 6. Allows for new frames to be generated after without looping

    Outputs:
        - samples (Latent)
    """
    _original_name: str = 'WanVideoSampler'

    def __init__(self, model: Slot[Any], image_embeds: Slot[Any], steps: int = 30, cfg: float = 6.0, shift: float = 5.0, seed: int = 0, force_offload: bool = True, scheduler: str = 'unipc', riflex_freq_index: int = 0):
        super().__init__(**{"model": model, "image_embeds": image_embeds, "steps": steps, "cfg": cfg, "shift": shift, "seed": seed, "force_offload": force_offload, "scheduler": scheduler, "riflex_freq_index": riflex_freq_index})
        self.inputs = WanVideoSamplerInputs(self)
        self.outputs = WanVideoSamplerOutputs(self)

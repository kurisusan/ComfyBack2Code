
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for LumaVideoNode
class LumaVideoNodeInputs(InputSlots):
    prompt: Slot[str]
    model: Slot[str]
    aspect_ratio: Slot[str]
    resolution: Slot[str]
    duration: Slot[str]
    loop: Slot[bool]
    seed: Slot[int]
    def __init__(self, node: "Node"):
        self.prompt = Slot[str](node, "prompt", 'STRING')
        self.model = Slot[str](node, "model", ['ray-2', 'ray-flash-2', 'ray-1-6'])
        self.aspect_ratio = Slot[str](node, "aspect_ratio", ['1:1', '16:9', '9:16', '4:3', '3:4', '21:9', '9:21'])
        self.resolution = Slot[str](node, "resolution", ['540p', '720p', '1080p', '4k'])
        self.duration = Slot[str](node, "duration", ['5s', '9s'])
        self.loop = Slot[bool](node, "loop", 'BOOLEAN')
        self.seed = Slot[int](node, "seed", 'INT')

class LumaVideoNodeOutputs(OutputSlots):
    video: Slot[Any]
    def __init__(self, node: "Node"):
        self.video = Slot[Any](node, "VIDEO", 'VIDEO')

class LumaVideoNode(Node[LumaVideoNodeInputs, LumaVideoNodeOutputs]):
    """
    Original name: LumaVideoNode
    Category: api node/video/Luma
    Generates videos synchronously based on prompt and output_size.

    Inputs:
        - prompt (str) (default: '')
          Prompt for the video generation
        - model (str)
        - aspect_ratio (str) (default: '16:9')
        - resolution (str) (default: '540p')
        - duration (str)
        - loop (bool) (default: False)
        - seed (int) (default: 0)
          Seed to determine if node should re-run; actual results are nondeterministic regardless of seed.

    Outputs:
        - video (Any)
    """
    _original_name: str = 'LumaVideoNode'

    def __init__(self, model: str, duration: str, prompt: str = '', aspect_ratio: str = '16:9', resolution: str = '540p', loop: bool = False, seed: int = 0):
        super().__init__(**{"prompt": prompt, "model": model, "aspect_ratio": aspect_ratio, "resolution": resolution, "duration": duration, "loop": loop, "seed": seed})
        self.inputs = LumaVideoNodeInputs(self)
        self.outputs = LumaVideoNodeOutputs(self)

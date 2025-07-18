
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for LumaImageToVideoNode
class LumaImageToVideoNodeInputs(InputSlots):
    prompt: Slot[str]
    model: Slot[str]
    resolution: Slot[str]
    duration: Slot[str]
    loop: Slot[bool]
    seed: Slot[int]
    def __init__(self, node: "Node"):
        self.prompt = Slot[str](node, "prompt", 'STRING')
        self.model = Slot[str](node, "model", ['ray-2', 'ray-flash-2', 'ray-1-6'])
        self.resolution = Slot[str](node, "resolution", ['540p', '720p', '1080p', '4k'])
        self.duration = Slot[str](node, "duration", ['5s', '9s'])
        self.loop = Slot[bool](node, "loop", 'BOOLEAN')
        self.seed = Slot[int](node, "seed", 'INT')

class LumaImageToVideoNodeOutputs(OutputSlots):
    video: Slot[Any]
    def __init__(self, node: "Node"):
        self.video = Slot[Any](node, "VIDEO", 'VIDEO')

class LumaImageToVideoNode(Node[LumaImageToVideoNodeInputs, LumaImageToVideoNodeOutputs]):
    """
    Original name: LumaImageToVideoNode
    Category: api node/video/Luma
    Generates videos synchronously based on prompt, input images, and output_size.

    Inputs:
        - prompt (str) (default: '')
          Prompt for the video generation
        - model (str)
        - resolution (str) (default: '540p')
        - duration (str)
        - loop (bool) (default: False)
        - seed (int) (default: 0)
          Seed to determine if node should re-run; actual results are nondeterministic regardless of seed.

    Outputs:
        - video (Any)
    """
    _original_name: str = 'LumaImageToVideoNode'

    def __init__(self, model: str, duration: str, prompt: str = '', resolution: str = '540p', loop: bool = False, seed: int = 0):
        super().__init__(**{"prompt": prompt, "model": model, "resolution": resolution, "duration": duration, "loop": loop, "seed": seed})
        self.inputs = LumaImageToVideoNodeInputs(self)
        self.outputs = LumaImageToVideoNodeOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for LumaImageModifyNode
class LumaImageModifyNodeInputs(InputSlots):
    image: Slot[Image]
    prompt: Slot[str]
    image_weight: Slot[float]
    model: Slot[str]
    seed: Slot[int]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.prompt = Slot[str](node, "prompt", 'STRING')
        self.image_weight = Slot[float](node, "image_weight", 'FLOAT')
        self.model = Slot[str](node, "model", ['photon-1', 'photon-flash-1'])
        self.seed = Slot[int](node, "seed", 'INT')

class LumaImageModifyNodeOutputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class LumaImageModifyNode(Node[LumaImageModifyNodeInputs, LumaImageModifyNodeOutputs]):
    """
    Original name: LumaImageModifyNode
    Category: api node/image/Luma
    Modifies images synchronously based on prompt and aspect ratio.

    Inputs:
        - image (Image)
        - prompt (str) (default: '')
          Prompt for the image generation
        - image_weight (float) (default: 0.1)
          Weight of the image; the closer to 1.0, the less the image will be modified.
        - model (str)
        - seed (int) (default: 0)
          Seed to determine if node should re-run; actual results are nondeterministic regardless of seed.

    Outputs:
        - image (Image)
    """
    _original_name: str = 'LumaImageModifyNode'

    def __init__(self, image: Slot[Image], model: str, prompt: str = '', image_weight: float = 0.1, seed: int = 0):
        super().__init__(**{"image": image, "prompt": prompt, "image_weight": image_weight, "model": model, "seed": seed})
        self.inputs = LumaImageModifyNodeInputs(self)
        self.outputs = LumaImageModifyNodeOutputs(self)

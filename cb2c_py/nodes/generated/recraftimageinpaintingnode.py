
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for RecraftImageInpaintingNode
class RecraftImageInpaintingNodeInputs(InputSlots):
    image: Slot[Image]
    mask: Slot[Image]
    prompt: Slot[str]
    n: Slot[int]
    seed: Slot[int]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.mask = Slot[Image](node, "mask", 'MASK')
        self.prompt = Slot[str](node, "prompt", 'STRING')
        self.n = Slot[int](node, "n", 'INT')
        self.seed = Slot[int](node, "seed", 'INT')

class RecraftImageInpaintingNodeOutputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class RecraftImageInpaintingNode(Node[RecraftImageInpaintingNodeInputs, RecraftImageInpaintingNodeOutputs]):
    """
    Original name: RecraftImageInpaintingNode
    Category: api node/image/Recraft
    Modify image based on prompt and mask.

    Inputs:
        - image (Image)
        - mask (Image)
        - prompt (str) (default: '')
          Prompt for the image generation.
        - n (int) (default: 1)
          The number of images to generate.
        - seed (int) (default: 0)
          Seed to determine if node should re-run; actual results are nondeterministic regardless of seed.

    Outputs:
        - image (Image)
    """
    _original_name: str = 'RecraftImageInpaintingNode'

    def __init__(self, image: Slot[Image], mask: Slot[Image], prompt: str = '', n: int = 1, seed: int = 0):
        super().__init__(**{"image": image, "mask": mask, "prompt": prompt, "n": n, "seed": seed})
        self.inputs = RecraftImageInpaintingNodeInputs(self)
        self.outputs = RecraftImageInpaintingNodeOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for KlingImageGenerationNode
class KlingImageGenerationNodeInputs(InputSlots):
    prompt: Slot[str]
    negative_prompt: Slot[str]
    image_type: Slot[str]
    image_fidelity: Slot[float]
    human_fidelity: Slot[float]
    model_name: Slot[str]
    aspect_ratio: Slot[str]
    n: Slot[int]
    def __init__(self, node: "Node"):
        self.prompt = Slot[str](node, "prompt", 'STRING')
        self.negative_prompt = Slot[str](node, "negative_prompt", 'STRING')
        self.image_type = Slot[str](node, "image_type", 'COMBO')
        self.image_fidelity = Slot[float](node, "image_fidelity", 'FLOAT')
        self.human_fidelity = Slot[float](node, "human_fidelity", 'FLOAT')
        self.model_name = Slot[str](node, "model_name", 'COMBO')
        self.aspect_ratio = Slot[str](node, "aspect_ratio", 'COMBO')
        self.n = Slot[int](node, "n", 'INT')

class KlingImageGenerationNodeOutputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class KlingImageGenerationNode(Node[KlingImageGenerationNodeInputs, KlingImageGenerationNodeOutputs]):
    """
    Original name: KlingImageGenerationNode
    Category: api node/image/Kling
    Kling Image Generation Node. Generate an image from a text prompt with an optional reference image.

    Inputs:
        - prompt (str)
          Positive text prompt
        - negative_prompt (str) (default: None)
          Negative text prompt
        - image_type (Any) (default: 'None')
        - image_fidelity (float) (default: 0.5)
          Reference intensity for user-uploaded images
        - human_fidelity (float) (default: 0.45)
          Subject reference similarity
        - model_name (Any) (default: 'kling-v1')
        - aspect_ratio (Any) (default: '16:9')
        - n (int) (default: 1)
          Number of generated images

    Outputs:
        - image (Image)
    """
    _original_name: str = 'KlingImageGenerationNode'

    def __init__(self, prompt: str, negative_prompt: str = None, image_type: str = 'None', image_fidelity: float = 0.5, human_fidelity: float = 0.45, model_name: str = 'kling-v1', aspect_ratio: str = '16:9', n: int = 1):
        super().__init__(**{"prompt": prompt, "negative_prompt": negative_prompt, "image_type": image_type, "image_fidelity": image_fidelity, "human_fidelity": human_fidelity, "model_name": model_name, "aspect_ratio": aspect_ratio, "n": n})
        self.inputs = KlingImageGenerationNodeInputs(self)
        self.outputs = KlingImageGenerationNodeOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for WanVideoImageClipEncode
class WanVideoImageClipEncodeInputs(InputSlots):
    clip_vision: Slot[Any]
    image: Slot[Image]
    vae: Slot[Any]
    generation_width: Slot[int]
    generation_height: Slot[int]
    num_frames: Slot[int]
    def __init__(self, node: "Node"):
        self.clip_vision = Slot[Any](node, "clip_vision", 'CLIP_VISION')
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.vae = Slot[Any](node, "vae", 'WANVAE')
        self.generation_width = Slot[int](node, "generation_width", 'INT')
        self.generation_height = Slot[int](node, "generation_height", 'INT')
        self.num_frames = Slot[int](node, "num_frames", 'INT')

class WanVideoImageClipEncodeOutputs(OutputSlots):
    image_embeds: Slot[Any]
    def __init__(self, node: "Node"):
        self.image_embeds = Slot[Any](node, "image_embeds", 'WANVIDIMAGE_EMBEDS')

class WanVideoImageClipEncode(Node[WanVideoImageClipEncodeInputs, WanVideoImageClipEncodeOutputs]):
    """
    Original name: WanVideoImageClipEncode
    Category: WanVideoWrapper
    

    Inputs:
        - clip_vision (Any)
        - image (Image)
          Image to encode
        - vae (Any)
        - generation_width (int) (default: 832)
          Width of the image to encode
        - generation_height (int) (default: 480)
          Height of the image to encode
        - num_frames (int) (default: 81)
          Number of frames to encode

    Outputs:
        - image_embeds (Any)
    """
    _original_name: str = 'WanVideoImageClipEncode'

    def __init__(self, clip_vision: Slot[Any], image: Slot[Image], vae: Slot[Any], generation_width: int = 832, generation_height: int = 480, num_frames: int = 81):
        super().__init__(**{"clip_vision": clip_vision, "image": image, "vae": vae, "generation_width": generation_width, "generation_height": generation_height, "num_frames": num_frames})
        self.inputs = WanVideoImageClipEncodeInputs(self)
        self.outputs = WanVideoImageClipEncodeOutputs(self)

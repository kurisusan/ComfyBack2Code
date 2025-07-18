
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ImagePreviewFromLatent_
class ImagePreviewFromLatent_Inputs(InputSlots):
    latent: Slot[Latent]
    vae: Slot[Vae]
    tile_size: Slot[int]
    def __init__(self, node: "Node"):
        self.latent = Slot[Latent](node, "latent", 'LATENT')
        self.vae = Slot[Vae](node, "vae", 'VAE')
        self.tile_size = Slot[int](node, "tile_size", 'INT')

class ImagePreviewFromLatent_Outputs(OutputSlots):
    image: Slot[Image]
    mask: Slot[Image]
    width: Slot[int]
    height: Slot[int]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')
        self.mask = Slot[Image](node, "MASK", 'MASK')
        self.width = Slot[int](node, "width", 'INT')
        self.height = Slot[int](node, "height", 'INT')

class ImagePreviewFromLatent_(Node[ImagePreviewFromLatent_Inputs, ImagePreviewFromLatent_Outputs]):
    """
    Original name: ImagePreviewFromLatent+
    Category: essentials/image utils
    Saves the input images to your ComfyUI output directory.

    Inputs:
        - latent (Latent)
        - vae (Vae)
        - tile_size (int) (default: 0)

    Outputs:
        - image (Image)
        - mask (Image)
        - width (int)
        - height (int)
    """
    _original_name: str = 'ImagePreviewFromLatent+'

    def __init__(self, latent: Slot[Latent], vae: Slot[Vae], tile_size: int = 0):
        super().__init__(**{"latent": latent, "vae": vae, "tile_size": tile_size})
        self.inputs = ImagePreviewFromLatent_Inputs(self)
        self.outputs = ImagePreviewFromLatent_Outputs(self)

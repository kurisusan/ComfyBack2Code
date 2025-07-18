
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for WanVideoDecode
class WanVideoDecodeInputs(InputSlots):
    vae: Slot[Any]
    samples: Slot[Latent]
    enable_vae_tiling: Slot[bool]
    tile_x: Slot[int]
    tile_y: Slot[int]
    tile_stride_x: Slot[int]
    tile_stride_y: Slot[int]
    def __init__(self, node: "Node"):
        self.vae = Slot[Any](node, "vae", 'WANVAE')
        self.samples = Slot[Latent](node, "samples", 'LATENT')
        self.enable_vae_tiling = Slot[bool](node, "enable_vae_tiling", 'BOOLEAN')
        self.tile_x = Slot[int](node, "tile_x", 'INT')
        self.tile_y = Slot[int](node, "tile_y", 'INT')
        self.tile_stride_x = Slot[int](node, "tile_stride_x", 'INT')
        self.tile_stride_y = Slot[int](node, "tile_stride_y", 'INT')

class WanVideoDecodeOutputs(OutputSlots):
    images: Slot[Image]
    def __init__(self, node: "Node"):
        self.images = Slot[Image](node, "images", 'IMAGE')

class WanVideoDecode(Node[WanVideoDecodeInputs, WanVideoDecodeOutputs]):
    """
    Original name: WanVideoDecode
    Category: WanVideoWrapper
    

    Inputs:
        - vae (Any)
        - samples (Latent)
        - enable_vae_tiling (bool) (default: False)
          Drastically reduces memory use but will introduce seams at tile stride boundaries. The location and number of seams is dictated by the tile stride size. The visibility of seams can be controlled by increasing the tile size. Seams become less obvious at 1.5x stride and are barely noticeable at 2x stride size. Which is to say if you use a stride width of 160, the seams are barely noticeable with a tile width of 320.
        - tile_x (int) (default: 272)
          Tile width in pixels. Smaller values use less VRAM but will make seams more obvious.
        - tile_y (int) (default: 272)
          Tile height in pixels. Smaller values use less VRAM but will make seams more obvious.
        - tile_stride_x (int) (default: 144)
          Tile stride width in pixels. Smaller values use less VRAM but will introduce more seams.
        - tile_stride_y (int) (default: 128)
          Tile stride height in pixels. Smaller values use less VRAM but will introduce more seams.

    Outputs:
        - images (Image)
    """
    _original_name: str = 'WanVideoDecode'

    def __init__(self, vae: Slot[Any], samples: Slot[Latent], enable_vae_tiling: bool = False, tile_x: int = 272, tile_y: int = 272, tile_stride_x: int = 144, tile_stride_y: int = 128):
        super().__init__(**{"vae": vae, "samples": samples, "enable_vae_tiling": enable_vae_tiling, "tile_x": tile_x, "tile_y": tile_y, "tile_stride_x": tile_stride_x, "tile_stride_y": tile_stride_y})
        self.inputs = WanVideoDecodeInputs(self)
        self.outputs = WanVideoDecodeOutputs(self)

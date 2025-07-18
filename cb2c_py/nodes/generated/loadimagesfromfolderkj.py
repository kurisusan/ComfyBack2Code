
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for LoadImagesFromFolderKJ
class LoadImagesFromFolderKJInputs(InputSlots):
    folder: Slot[str]
    width: Slot[int]
    height: Slot[int]
    keep_aspect_ratio: Slot[str]
    def __init__(self, node: "Node"):
        self.folder = Slot[str](node, "folder", 'STRING')
        self.width = Slot[int](node, "width", 'INT')
        self.height = Slot[int](node, "height", 'INT')
        self.keep_aspect_ratio = Slot[str](node, "keep_aspect_ratio", ['crop', 'pad', 'stretch'])

class LoadImagesFromFolderKJOutputs(OutputSlots):
    image: Slot[Image]
    mask: Slot[Image]
    count: Slot[int]
    image_path: Slot[str]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.mask = Slot[Image](node, "mask", 'MASK')
        self.count = Slot[int](node, "count", 'INT')
        self.image_path = Slot[str](node, "image_path", 'STRING')

class LoadImagesFromFolderKJ(Node[LoadImagesFromFolderKJInputs, LoadImagesFromFolderKJOutputs]):
    """
    Original name: LoadImagesFromFolderKJ
    Category: KJNodes/image
    Loads images from a folder into a batch, images are resized and loaded into a batch.

    Inputs:
        - folder (str) (default: '')
        - width (int) (default: 1024)
        - height (int) (default: 1024)
        - keep_aspect_ratio (str)

    Outputs:
        - image (Image)
        - mask (Image)
        - count (int)
        - image_path (str)
    """
    _original_name: str = 'LoadImagesFromFolderKJ'

    def __init__(self, keep_aspect_ratio: str, folder: str = '', width: int = 1024, height: int = 1024):
        super().__init__(**{"folder": folder, "width": width, "height": height, "keep_aspect_ratio": keep_aspect_ratio})
        self.inputs = LoadImagesFromFolderKJInputs(self)
        self.outputs = LoadImagesFromFolderKJOutputs(self)

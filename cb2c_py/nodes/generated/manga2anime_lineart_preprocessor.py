
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for Manga2Anime_LineArt_Preprocessor
class Manga2Anime_LineArt_PreprocessorInputs(InputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')

class Manga2Anime_LineArt_PreprocessorOutputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class Manga2Anime_LineArt_Preprocessor(Node[Manga2Anime_LineArt_PreprocessorInputs, Manga2Anime_LineArt_PreprocessorOutputs]):
    """
    Original name: Manga2Anime_LineArt_Preprocessor
    Category: ControlNet Preprocessors/Line Extractors
    

    Inputs:
        - image (Image)

    Outputs:
        - image (Image)
    """
    _original_name: str = 'Manga2Anime_LineArt_Preprocessor'

    def __init__(self, image: Slot[Image]):
        super().__init__(**{"image": image})
        self.inputs = Manga2Anime_LineArt_PreprocessorInputs(self)
        self.outputs = Manga2Anime_LineArt_PreprocessorOutputs(self)

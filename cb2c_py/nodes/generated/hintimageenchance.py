
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for HintImageEnchance
class HintImageEnchanceInputs(InputSlots):
    hint_image: Slot[Image]
    image_gen_width: Slot[int]
    image_gen_height: Slot[int]
    resize_mode: Slot[str]
    def __init__(self, node: "Node"):
        self.hint_image = Slot[Image](node, "hint_image", 'IMAGE')
        self.image_gen_width = Slot[int](node, "image_gen_width", 'INT')
        self.image_gen_height = Slot[int](node, "image_gen_height", 'INT')
        self.resize_mode = Slot[str](node, "resize_mode", ['Just Resize', 'Crop and Resize', 'Resize and Fill'])

class HintImageEnchanceOutputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "IMAGE", 'IMAGE')

class HintImageEnchance(Node[HintImageEnchanceInputs, HintImageEnchanceOutputs]):
    """
    Original name: HintImageEnchance
    Category: ControlNet Preprocessors
    

    Inputs:
        - hint_image (Image)
        - image_gen_width (int) (default: 512)
        - image_gen_height (int) (default: 512)
        - resize_mode (str) (default: 'Just Resize')

    Outputs:
        - image (Image)
    """
    _original_name: str = 'HintImageEnchance'

    def __init__(self, hint_image: Slot[Image], image_gen_width: int = 512, image_gen_height: int = 512, resize_mode: str = 'Just Resize'):
        super().__init__(**{"hint_image": hint_image, "image_gen_width": image_gen_width, "image_gen_height": image_gen_height, "resize_mode": resize_mode})
        self.inputs = HintImageEnchanceInputs(self)
        self.outputs = HintImageEnchanceOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for PhotoMakerEncode
class PhotoMakerEncodeInputs(InputSlots):
    photomaker: Slot[Any]
    image: Slot[Image]
    clip: Slot[Clip]
    text: Slot[str]
    def __init__(self, node: "Node"):
        self.photomaker = Slot[Any](node, "photomaker", 'PHOTOMAKER')
        self.image = Slot[Image](node, "image", 'IMAGE')
        self.clip = Slot[Clip](node, "clip", 'CLIP')
        self.text = Slot[str](node, "text", 'STRING')

class PhotoMakerEncodeOutputs(OutputSlots):
    conditioning: Slot[Conditioning]
    def __init__(self, node: "Node"):
        self.conditioning = Slot[Conditioning](node, "CONDITIONING", 'CONDITIONING')

class PhotoMakerEncode(Node[PhotoMakerEncodeInputs, PhotoMakerEncodeOutputs]):
    """
    Original name: PhotoMakerEncode
    Category: _for_testing/photomaker
    

    Inputs:
        - photomaker (Any)
        - image (Image)
        - clip (Clip)
        - text (str) (default: 'photograph of photomaker')

    Outputs:
        - conditioning (Conditioning)
    """
    _original_name: str = 'PhotoMakerEncode'

    def __init__(self, photomaker: Slot[Any], image: Slot[Image], clip: Slot[Clip], text: str = 'photograph of photomaker'):
        super().__init__(**{"photomaker": photomaker, "image": image, "clip": clip, "text": text})
        self.inputs = PhotoMakerEncodeInputs(self)
        self.outputs = PhotoMakerEncodeOutputs(self)

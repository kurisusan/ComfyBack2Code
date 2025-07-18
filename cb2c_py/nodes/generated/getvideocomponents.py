
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for GetVideoComponents
class GetVideoComponentsInputs(InputSlots):
    video: Slot[Any]
    def __init__(self, node: "Node"):
        self.video = Slot[Any](node, "video", 'VIDEO')

class GetVideoComponentsOutputs(OutputSlots):
    images: Slot[Image]
    audio: Slot[Any]
    fps: Slot[float]
    def __init__(self, node: "Node"):
        self.images = Slot[Image](node, "images", 'IMAGE')
        self.audio = Slot[Any](node, "audio", 'AUDIO')
        self.fps = Slot[float](node, "fps", 'FLOAT')

class GetVideoComponents(Node[GetVideoComponentsInputs, GetVideoComponentsOutputs]):
    """
    Original name: GetVideoComponents
    Category: image/video
    Extracts all components from a video: frames, audio, and framerate.

    Inputs:
        - video (Any)
          The video to extract components from.

    Outputs:
        - images (Image)
        - audio (Any)
        - fps (float)
    """
    _original_name: str = 'GetVideoComponents'

    def __init__(self, video: Slot[Any]):
        super().__init__(**{"video": video})
        self.inputs = GetVideoComponentsInputs(self)
        self.outputs = GetVideoComponentsOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SaveVideo
class SaveVideoInputs(InputSlots):
    video: Slot[Any]
    filename_prefix: Slot[str]
    format: Slot[str]
    codec: Slot[str]
    def __init__(self, node: "Node"):
        self.video = Slot[Any](node, "video", 'VIDEO')
        self.filename_prefix = Slot[str](node, "filename_prefix", 'STRING')
        self.format = Slot[str](node, "format", ['auto', 'mp4'])
        self.codec = Slot[str](node, "codec", ['auto', 'h264'])

class SaveVideoOutputs(OutputSlots):

    def __init__(self, node: "Node"):
        pass

class SaveVideo(Node[SaveVideoInputs, SaveVideoOutputs]):
    """
    Original name: SaveVideo
    Category: image/video
    Saves the input images to your ComfyUI output directory.

    Inputs:
        - video (Any)
          The video to save.
        - filename_prefix (str) (default: 'video/ComfyUI')
          The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes.
        - format (str) (default: 'auto')
          The format to save the video as.
        - codec (str) (default: 'auto')
          The codec to use for the video.

    Outputs:
        No outputs.
    """
    _original_name: str = 'SaveVideo'

    def __init__(self, video: Slot[Any], filename_prefix: str = 'video/ComfyUI', format: str = 'auto', codec: str = 'auto'):
        super().__init__(**{"video": video, "filename_prefix": filename_prefix, "format": format, "codec": codec})
        self.inputs = SaveVideoInputs(self)
        self.outputs = SaveVideoOutputs(self)

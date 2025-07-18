
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for VHS_VideoInfoSource
class VHS_VideoInfoSourceInputs(InputSlots):
    video_info: Slot[Any]
    def __init__(self, node: "Node"):
        self.video_info = Slot[Any](node, "video_info", 'VHS_VIDEOINFO')

class VHS_VideoInfoSourceOutputs(OutputSlots):
    fps_: Slot[float]
    frame_count_: Slot[int]
    duration_: Slot[float]
    width_: Slot[int]
    height_: Slot[int]
    def __init__(self, node: "Node"):
        self.fps_ = Slot[float](node, "fps🟨", 'FLOAT')
        self.frame_count_ = Slot[int](node, "frame_count🟨", 'INT')
        self.duration_ = Slot[float](node, "duration🟨", 'FLOAT')
        self.width_ = Slot[int](node, "width🟨", 'INT')
        self.height_ = Slot[int](node, "height🟨", 'INT')

class VHS_VideoInfoSource(Node[VHS_VideoInfoSourceInputs, VHS_VideoInfoSourceOutputs]):
    """
    Original name: VHS_VideoInfoSource
    Category: Video Helper Suite 🎥🅥🅗🅢
    Video Info Source 🎥🅥🅗🅢<div style="font-size: 0.8em"><div id=VHS_shortdesc>Splits information on a video into a numerous outputs describing the file itself without accounting for load options</div></div><div style="font-size: 0.8em"><div vhs_title="Inputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Inputs: <div vhs_title="video_info" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">video_info: A connection to a Load Video node</div></div></div></div><div vhs_title="Outputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Outputs: <div vhs_title="source_fps🟨" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">source_fps🟨: The frame rate of the video</div></div><div vhs_title="source_frame_count🟨" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">source_frame_count🟨: How many total frames the video contains before accounting for frame rate or select_every_nth</div></div><div vhs_title="source_duration🟨" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">source_duration🟨: The length of images just returned in seconds</div></div><div vhs_title="source_width🟨" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">source_width🟨: The original width</div></div><div vhs_title="source_height🟨" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">source_height🟨: The original height</div></div></div></div></div>

    Inputs:
        - video_info (Any)

    Outputs:
        - fps_ (float)
        - frame_count_ (int)
        - duration_ (float)
        - width_ (int)
        - height_ (int)
    """
    _original_name: str = 'VHS_VideoInfoSource'

    def __init__(self, video_info: Slot[Any]):
        super().__init__(**{"video_info": video_info})
        self.inputs = VHS_VideoInfoSourceInputs(self)
        self.outputs = VHS_VideoInfoSourceOutputs(self)

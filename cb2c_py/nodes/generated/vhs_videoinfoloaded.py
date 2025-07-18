
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for VHS_VideoInfoLoaded
class VHS_VideoInfoLoadedInputs(InputSlots):
    video_info: Slot[Any]
    def __init__(self, node: "Node"):
        self.video_info = Slot[Any](node, "video_info", 'VHS_VIDEOINFO')

class VHS_VideoInfoLoadedOutputs(OutputSlots):
    fps_: Slot[float]
    frame_count_: Slot[int]
    duration_: Slot[float]
    width_: Slot[int]
    height_: Slot[int]
    def __init__(self, node: "Node"):
        self.fps_ = Slot[float](node, "fps🟦", 'FLOAT')
        self.frame_count_ = Slot[int](node, "frame_count🟦", 'INT')
        self.duration_ = Slot[float](node, "duration🟦", 'FLOAT')
        self.width_ = Slot[int](node, "width🟦", 'INT')
        self.height_ = Slot[int](node, "height🟦", 'INT')

class VHS_VideoInfoLoaded(Node[VHS_VideoInfoLoadedInputs, VHS_VideoInfoLoadedOutputs]):
    """
    Original name: VHS_VideoInfoLoaded
    Category: Video Helper Suite 🎥🅥🅗🅢
    Video Info Loaded 🎥🅥🅗🅢<div style="font-size: 0.8em"><div id=VHS_shortdesc>Splits information on a video into a numerous outputs describing the file itself after accounting for load options</div></div><div style="font-size: 0.8em"><div vhs_title="Inputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Inputs: <div vhs_title="video_info" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">video_info: A connection to a Load Video node</div></div></div></div><div vhs_title="Outputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Outputs: <div vhs_title="loaded_fps🟦" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">loaded_fps🟦: The frame rate after accounting for force_rate and select_every_nth. This output is of particular use as it can be connected to the converted frame_rate input of a Video Combine node to ensure audio remains synchronized.</div></div><div vhs_title="loaded_frame_count🟦" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">loaded_frame_count🟦: The number of frames returned by the current execution. Identical to the frame_count returned by the node itself</div></div><div vhs_title="loaded_duration🟦" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">loaded_duration🟦: The duration in seconds of returned images after accounting for frame_load_cap</div></div><div vhs_title="loaded_width🟦" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">loaded_width🟦: The width of the video after scaling. This is the dimension of the corresponding image even if loading as a latent directly</div></div><div vhs_title="loaded_height🟦" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">loaded_height🟦: The height of the video after scaling. This is the dimension of the corresponding image even if loading as a latent directly</div></div></div></div></div>

    Inputs:
        - video_info (Any)

    Outputs:
        - fps_ (float)
        - frame_count_ (int)
        - duration_ (float)
        - width_ (int)
        - height_ (int)
    """
    _original_name: str = 'VHS_VideoInfoLoaded'

    def __init__(self, video_info: Slot[Any]):
        super().__init__(**{"video_info": video_info})
        self.inputs = VHS_VideoInfoLoadedInputs(self)
        self.outputs = VHS_VideoInfoLoadedOutputs(self)

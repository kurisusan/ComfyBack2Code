
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for KlingVideoExtendNode
class KlingVideoExtendNodeInputs(InputSlots):
    prompt: Slot[str]
    negative_prompt: Slot[str]
    cfg_scale: Slot[float]
    video_id: Slot[str]
    def __init__(self, node: "Node"):
        self.prompt = Slot[str](node, "prompt", 'STRING')
        self.negative_prompt = Slot[str](node, "negative_prompt", 'STRING')
        self.cfg_scale = Slot[float](node, "cfg_scale", 'FLOAT')
        self.video_id = Slot[str](node, "video_id", 'STRING')

class KlingVideoExtendNodeOutputs(OutputSlots):
    video: Slot[Any]
    video_id: Slot[str]
    duration: Slot[str]
    def __init__(self, node: "Node"):
        self.video = Slot[Any](node, "VIDEO", 'VIDEO')
        self.video_id = Slot[str](node, "video_id", 'STRING')
        self.duration = Slot[str](node, "duration", 'STRING')

class KlingVideoExtendNode(Node[KlingVideoExtendNodeInputs, KlingVideoExtendNodeOutputs]):
    """
    Original name: KlingVideoExtendNode
    Category: api node/video/Kling
    Kling Video Extend Node. Extend videos made by other Kling nodes. The video_id is created by using other Kling Nodes.

    Inputs:
        - prompt (str) (default: None)
          Positive text prompt for guiding the video extension
        - negative_prompt (str) (default: None)
          Negative text prompt for elements to avoid in the extended video
        - cfg_scale (float) (default: 0.5)
        - video_id (str) (default: None)
          The ID of the video to be extended. Supports videos generated by text-to-video, image-to-video, and previous video extension operations. Cannot exceed 3 minutes total duration after extension.

    Outputs:
        - video (Any)
        - video_id (str)
        - duration (str)
    """
    _original_name: str = 'KlingVideoExtendNode'

    def __init__(self, prompt: str = None, negative_prompt: str = None, cfg_scale: float = 0.5, video_id: str = None):
        super().__init__(**{"prompt": prompt, "negative_prompt": negative_prompt, "cfg_scale": cfg_scale, "video_id": video_id})
        self.inputs = KlingVideoExtendNodeInputs(self)
        self.outputs = KlingVideoExtendNodeOutputs(self)

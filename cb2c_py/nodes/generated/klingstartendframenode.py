
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for KlingStartEndFrameNode
class KlingStartEndFrameNodeInputs(InputSlots):
    start_frame: Slot[Image]
    end_frame: Slot[Image]
    prompt: Slot[str]
    negative_prompt: Slot[str]
    cfg_scale: Slot[float]
    aspect_ratio: Slot[str]
    mode: Slot[str]
    def __init__(self, node: "Node"):
        self.start_frame = Slot[Image](node, "start_frame", 'IMAGE')
        self.end_frame = Slot[Image](node, "end_frame", 'IMAGE')
        self.prompt = Slot[str](node, "prompt", 'STRING')
        self.negative_prompt = Slot[str](node, "negative_prompt", 'STRING')
        self.cfg_scale = Slot[float](node, "cfg_scale", 'FLOAT')
        self.aspect_ratio = Slot[str](node, "aspect_ratio", 'COMBO')
        self.mode = Slot[str](node, "mode", ['standard mode / 5s duration / kling-v1', 'pro mode / 5s duration / kling-v1', 'pro mode / 5s duration / kling-v1-5', 'pro mode / 10s duration / kling-v1-5', 'pro mode / 5s duration / kling-v1-6', 'pro mode / 10s duration / kling-v1-6'])

class KlingStartEndFrameNodeOutputs(OutputSlots):
    video: Slot[Any]
    video_id: Slot[str]
    duration: Slot[str]
    def __init__(self, node: "Node"):
        self.video = Slot[Any](node, "VIDEO", 'VIDEO')
        self.video_id = Slot[str](node, "video_id", 'STRING')
        self.duration = Slot[str](node, "duration", 'STRING')

class KlingStartEndFrameNode(Node[KlingStartEndFrameNodeInputs, KlingStartEndFrameNodeOutputs]):
    """
    Original name: KlingStartEndFrameNode
    Category: api node/video/Kling
    Generate a video sequence that transitions between your provided start and end images. The node creates all frames in between, producing a smooth transformation from the first frame to the last.

    Inputs:
        - start_frame (Image) (default: None)
          Reference Image - URL or Base64 encoded string, cannot exceed 10MB, resolution not less than 300*300px, aspect ratio between 1:2.5 ~ 2.5:1. Base64 should not include data:image prefix.
        - end_frame (Image) (default: None)
          Reference Image - End frame control. URL or Base64 encoded string, cannot exceed 10MB, resolution not less than 300*300px. Base64 should not include data:image prefix.
        - prompt (str) (default: None)
          Positive text prompt
        - negative_prompt (str) (default: None)
          Negative text prompt
        - cfg_scale (float) (default: 0.5)
        - aspect_ratio (Any) (default: '16:9')
        - mode (str) (default: 'pro mode / 5s duration / kling-v1-5')
          The configuration to use for the video generation following the format: mode / duration / model_name.

    Outputs:
        - video (Any)
        - video_id (str)
        - duration (str)
    """
    _original_name: str = 'KlingStartEndFrameNode'

    def __init__(self, start_frame: Slot[Image] = None, end_frame: Slot[Image] = None, prompt: str = None, negative_prompt: str = None, cfg_scale: float = 0.5, aspect_ratio: str = '16:9', mode: str = 'pro mode / 5s duration / kling-v1-5'):
        super().__init__(**{"start_frame": start_frame, "end_frame": end_frame, "prompt": prompt, "negative_prompt": negative_prompt, "cfg_scale": cfg_scale, "aspect_ratio": aspect_ratio, "mode": mode})
        self.inputs = KlingStartEndFrameNodeInputs(self)
        self.outputs = KlingStartEndFrameNodeOutputs(self)

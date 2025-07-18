
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for MultiTalkWav2VecEmbeds
class MultiTalkWav2VecEmbedsInputs(InputSlots):
    wav2vec_model: Slot[Any]
    audio_1: Slot[Any]
    normalize_loudness: Slot[bool]
    num_frames: Slot[int]
    fps: Slot[float]
    audio_scale: Slot[float]
    audio_cfg_scale: Slot[float]
    multi_audio_type: Slot[str]
    def __init__(self, node: "Node"):
        self.wav2vec_model = Slot[Any](node, "wav2vec_model", 'WAV2VECMODEL')
        self.audio_1 = Slot[Any](node, "audio_1", 'AUDIO')
        self.normalize_loudness = Slot[bool](node, "normalize_loudness", 'BOOLEAN')
        self.num_frames = Slot[int](node, "num_frames", 'INT')
        self.fps = Slot[float](node, "fps", 'FLOAT')
        self.audio_scale = Slot[float](node, "audio_scale", 'FLOAT')
        self.audio_cfg_scale = Slot[float](node, "audio_cfg_scale", 'FLOAT')
        self.multi_audio_type = Slot[str](node, "multi_audio_type", ['para', 'add'])

class MultiTalkWav2VecEmbedsOutputs(OutputSlots):
    multitalk_embeds: Slot[Any]
    audio: Slot[Any]
    def __init__(self, node: "Node"):
        self.multitalk_embeds = Slot[Any](node, "multitalk_embeds", 'MULTITALK_EMBEDS')
        self.audio = Slot[Any](node, "audio", 'AUDIO')

class MultiTalkWav2VecEmbeds(Node[MultiTalkWav2VecEmbedsInputs, MultiTalkWav2VecEmbedsOutputs]):
    """
    Original name: MultiTalkWav2VecEmbeds
    Category: WanVideoWrapper
    

    Inputs:
        - wav2vec_model (Any)
        - audio_1 (Any)
        - normalize_loudness (bool) (default: True)
        - num_frames (int) (default: 81)
        - fps (float) (default: 25.0)
        - audio_scale (float) (default: 1.0)
          Strength of the audio conditioning
        - audio_cfg_scale (float) (default: 1.0)
          When not 1.0, an extra model pass without audio conditioning is done: slower inference but more motion is allowed
        - multi_audio_type (str) (default: 'para')
          'para' overlay speakers in parallel, 'add' concatenate sequentially

    Outputs:
        - multitalk_embeds (Any)
        - audio (Any)
    """
    _original_name: str = 'MultiTalkWav2VecEmbeds'

    def __init__(self, wav2vec_model: Slot[Any], audio_1: Slot[Any], normalize_loudness: bool = True, num_frames: int = 81, fps: float = 25.0, audio_scale: float = 1.0, audio_cfg_scale: float = 1.0, multi_audio_type: str = 'para'):
        super().__init__(**{"wav2vec_model": wav2vec_model, "audio_1": audio_1, "normalize_loudness": normalize_loudness, "num_frames": num_frames, "fps": fps, "audio_scale": audio_scale, "audio_cfg_scale": audio_cfg_scale, "multi_audio_type": multi_audio_type})
        self.inputs = MultiTalkWav2VecEmbedsInputs(self)
        self.outputs = MultiTalkWav2VecEmbedsOutputs(self)

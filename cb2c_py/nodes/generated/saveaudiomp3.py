
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SaveAudioMP3
class SaveAudioMP3Inputs(InputSlots):
    audio: Slot[Any]
    filename_prefix: Slot[str]
    quality: Slot[str]
    def __init__(self, node: "Node"):
        self.audio = Slot[Any](node, "audio", 'AUDIO')
        self.filename_prefix = Slot[str](node, "filename_prefix", 'STRING')
        self.quality = Slot[str](node, "quality", ['V0', '128k', '320k'])

class SaveAudioMP3Outputs(OutputSlots):

    def __init__(self, node: "Node"):
        pass

class SaveAudioMP3(Node[SaveAudioMP3Inputs, SaveAudioMP3Outputs]):
    """
    Original name: SaveAudioMP3
    Category: audio
    

    Inputs:
        - audio (Any)
        - filename_prefix (str) (default: 'audio/ComfyUI')
        - quality (str) (default: 'V0')

    Outputs:
        No outputs.
    """
    _original_name: str = 'SaveAudioMP3'

    def __init__(self, audio: Slot[Any], filename_prefix: str = 'audio/ComfyUI', quality: str = 'V0'):
        super().__init__(**{"audio": audio, "filename_prefix": filename_prefix, "quality": quality})
        self.inputs = SaveAudioMP3Inputs(self)
        self.outputs = SaveAudioMP3Outputs(self)

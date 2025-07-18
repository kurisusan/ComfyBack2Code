
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SaveAudioOpus
class SaveAudioOpusInputs(InputSlots):
    audio: Slot[Any]
    filename_prefix: Slot[str]
    quality: Slot[str]
    def __init__(self, node: "Node"):
        self.audio = Slot[Any](node, "audio", 'AUDIO')
        self.filename_prefix = Slot[str](node, "filename_prefix", 'STRING')
        self.quality = Slot[str](node, "quality", ['64k', '96k', '128k', '192k', '320k'])

class SaveAudioOpusOutputs(OutputSlots):

    def __init__(self, node: "Node"):
        pass

class SaveAudioOpus(Node[SaveAudioOpusInputs, SaveAudioOpusOutputs]):
    """
    Original name: SaveAudioOpus
    Category: audio
    

    Inputs:
        - audio (Any)
        - filename_prefix (str) (default: 'audio/ComfyUI')
        - quality (str) (default: '128k')

    Outputs:
        No outputs.
    """
    _original_name: str = 'SaveAudioOpus'

    def __init__(self, audio: Slot[Any], filename_prefix: str = 'audio/ComfyUI', quality: str = '128k'):
        super().__init__(**{"audio": audio, "filename_prefix": filename_prefix, "quality": quality})
        self.inputs = SaveAudioOpusInputs(self)
        self.outputs = SaveAudioOpusOutputs(self)

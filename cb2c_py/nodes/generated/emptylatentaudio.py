
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for EmptyLatentAudio
class EmptyLatentAudioInputs(InputSlots):
    seconds: Slot[float]
    batch_size: Slot[int]
    def __init__(self, node: "Node"):
        self.seconds = Slot[float](node, "seconds", 'FLOAT')
        self.batch_size = Slot[int](node, "batch_size", 'INT')

class EmptyLatentAudioOutputs(OutputSlots):
    latent: Slot[Latent]
    def __init__(self, node: "Node"):
        self.latent = Slot[Latent](node, "LATENT", 'LATENT')

class EmptyLatentAudio(Node[EmptyLatentAudioInputs, EmptyLatentAudioOutputs]):
    """
    Original name: EmptyLatentAudio
    Category: latent/audio
    

    Inputs:
        - seconds (float) (default: 47.6)
        - batch_size (int) (default: 1)
          The number of latent images in the batch.

    Outputs:
        - latent (Latent)
    """
    _original_name: str = 'EmptyLatentAudio'

    def __init__(self, seconds: float = 47.6, batch_size: int = 1):
        super().__init__(**{"seconds": seconds, "batch_size": batch_size})
        self.inputs = EmptyLatentAudioInputs(self)
        self.outputs = EmptyLatentAudioOutputs(self)

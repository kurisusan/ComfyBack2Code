
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for GetLatentsFromBatchIndexed
class GetLatentsFromBatchIndexedInputs(InputSlots):
    latents: Slot[Latent]
    indexes: Slot[str]
    latent_format: Slot[str]
    def __init__(self, node: "Node"):
        self.latents = Slot[Latent](node, "latents", 'LATENT')
        self.indexes = Slot[str](node, "indexes", 'STRING')
        self.latent_format = Slot[str](node, "latent_format", ['BCHW', 'BTCHW', 'BCTHW'])

class GetLatentsFromBatchIndexedOutputs(OutputSlots):
    latent: Slot[Latent]
    def __init__(self, node: "Node"):
        self.latent = Slot[Latent](node, "LATENT", 'LATENT')

class GetLatentsFromBatchIndexed(Node[GetLatentsFromBatchIndexedInputs, GetLatentsFromBatchIndexedOutputs]):
    """
    Original name: GetLatentsFromBatchIndexed
    Category: KJNodes/latents
    
Selects and returns the latents at the specified indices as an latent batch.


    Inputs:
        - latents (Latent)
        - indexes (str) (default: '0, 1, 2')
        - latent_format (str) (default: 'BCHW')

    Outputs:
        - latent (Latent)
    """
    _original_name: str = 'GetLatentsFromBatchIndexed'

    def __init__(self, latents: Slot[Latent], indexes: str = '0, 1, 2', latent_format: str = 'BCHW'):
        super().__init__(**{"latents": latents, "indexes": indexes, "latent_format": latent_format})
        self.inputs = GetLatentsFromBatchIndexedInputs(self)
        self.outputs = GetLatentsFromBatchIndexedOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for CondPassThrough
class CondPassThroughInputs(InputSlots):

    def __init__(self, node: "Node"):
        pass

class CondPassThroughOutputs(OutputSlots):
    positive: Slot[Conditioning]
    negative: Slot[Conditioning]
    def __init__(self, node: "Node"):
        self.positive = Slot[Conditioning](node, "positive", 'CONDITIONING')
        self.negative = Slot[Conditioning](node, "negative", 'CONDITIONING')

class CondPassThrough(Node[CondPassThroughInputs, CondPassThroughOutputs]):
    """
    Original name: CondPassThrough
    Category: KJNodes/misc
    
    Simply passes through the positive and negative conditioning,
    workaround for Set node not allowing bypassed inputs.


    Inputs:
        No inputs.

    Outputs:
        - positive (Conditioning)
        - negative (Conditioning)
    """
    _original_name: str = 'CondPassThrough'

    def __init__(self, ):
        super().__init__(**{})
        self.inputs = CondPassThroughInputs(self)
        self.outputs = CondPassThroughOutputs(self)

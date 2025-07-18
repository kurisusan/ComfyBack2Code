
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SimpleMathFloat_
class SimpleMathFloat_Inputs(InputSlots):
    value: Slot[float]
    def __init__(self, node: "Node"):
        self.value = Slot[float](node, "value", 'FLOAT')

class SimpleMathFloat_Outputs(OutputSlots):
    float: Slot[float]
    def __init__(self, node: "Node"):
        self.float = Slot[float](node, "FLOAT", 'FLOAT')

class SimpleMathFloat_(Node[SimpleMathFloat_Inputs, SimpleMathFloat_Outputs]):
    """
    Original name: SimpleMathFloat+
    Category: essentials/utilities
    

    Inputs:
        - value (float) (default: 0.0)

    Outputs:
        - float (float)
    """
    _original_name: str = 'SimpleMathFloat+'

    def __init__(self, value: float = 0.0):
        super().__init__(**{"value": value})
        self.inputs = SimpleMathFloat_Inputs(self)
        self.outputs = SimpleMathFloat_Outputs(self)

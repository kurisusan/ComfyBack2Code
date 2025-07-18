
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ConditioningSetAreaStrength
class ConditioningSetAreaStrengthInputs(InputSlots):
    conditioning: Slot[Conditioning]
    strength: Slot[float]
    def __init__(self, node: "Node"):
        self.conditioning = Slot[Conditioning](node, "conditioning", 'CONDITIONING')
        self.strength = Slot[float](node, "strength", 'FLOAT')

class ConditioningSetAreaStrengthOutputs(OutputSlots):
    conditioning: Slot[Conditioning]
    def __init__(self, node: "Node"):
        self.conditioning = Slot[Conditioning](node, "CONDITIONING", 'CONDITIONING')

class ConditioningSetAreaStrength(Node[ConditioningSetAreaStrengthInputs, ConditioningSetAreaStrengthOutputs]):
    """
    Original name: ConditioningSetAreaStrength
    Category: conditioning
    

    Inputs:
        - conditioning (Conditioning)
        - strength (float) (default: 1.0)

    Outputs:
        - conditioning (Conditioning)
    """
    _original_name: str = 'ConditioningSetAreaStrength'

    def __init__(self, conditioning: Slot[Conditioning], strength: float = 1.0):
        super().__init__(**{"conditioning": conditioning, "strength": strength})
        self.inputs = ConditioningSetAreaStrengthInputs(self)
        self.outputs = ConditioningSetAreaStrengthOutputs(self)

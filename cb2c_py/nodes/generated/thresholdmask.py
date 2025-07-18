
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ThresholdMask
class ThresholdMaskInputs(InputSlots):
    mask: Slot[Image]
    value: Slot[float]
    def __init__(self, node: "Node"):
        self.mask = Slot[Image](node, "mask", 'MASK')
        self.value = Slot[float](node, "value", 'FLOAT')

class ThresholdMaskOutputs(OutputSlots):
    mask: Slot[Image]
    def __init__(self, node: "Node"):
        self.mask = Slot[Image](node, "MASK", 'MASK')

class ThresholdMask(Node[ThresholdMaskInputs, ThresholdMaskOutputs]):
    """
    Original name: ThresholdMask
    Category: mask
    

    Inputs:
        - mask (Image)
        - value (float) (default: 0.5)

    Outputs:
        - mask (Image)
    """
    _original_name: str = 'ThresholdMask'

    def __init__(self, mask: Slot[Image], value: float = 0.5):
        super().__init__(**{"mask": mask, "value": value})
        self.inputs = ThresholdMaskInputs(self)
        self.outputs = ThresholdMaskOutputs(self)

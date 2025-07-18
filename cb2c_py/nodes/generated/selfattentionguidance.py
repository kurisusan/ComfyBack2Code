
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SelfAttentionGuidance
class SelfAttentionGuidanceInputs(InputSlots):
    model: Slot[Model]
    scale: Slot[float]
    blur_sigma: Slot[float]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')
        self.scale = Slot[float](node, "scale", 'FLOAT')
        self.blur_sigma = Slot[float](node, "blur_sigma", 'FLOAT')

class SelfAttentionGuidanceOutputs(OutputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "MODEL", 'MODEL')

class SelfAttentionGuidance(Node[SelfAttentionGuidanceInputs, SelfAttentionGuidanceOutputs]):
    """
    Original name: SelfAttentionGuidance
    Category: _for_testing
    

    Inputs:
        - model (Model)
        - scale (float) (default: 0.5)
        - blur_sigma (float) (default: 2.0)

    Outputs:
        - model (Model)
    """
    _original_name: str = 'SelfAttentionGuidance'

    def __init__(self, model: Slot[Model], scale: float = 0.5, blur_sigma: float = 2.0):
        super().__init__(**{"model": model, "scale": scale, "blur_sigma": blur_sigma})
        self.inputs = SelfAttentionGuidanceInputs(self)
        self.outputs = SelfAttentionGuidanceOutputs(self)

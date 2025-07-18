
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for WanVideoNAG
class WanVideoNAGInputs(InputSlots):
    model: Slot[Model]
    conditioning: Slot[Conditioning]
    nag_scale: Slot[float]
    nag_alpha: Slot[float]
    nag_tau: Slot[float]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')
        self.conditioning = Slot[Conditioning](node, "conditioning", 'CONDITIONING')
        self.nag_scale = Slot[float](node, "nag_scale", 'FLOAT')
        self.nag_alpha = Slot[float](node, "nag_alpha", 'FLOAT')
        self.nag_tau = Slot[float](node, "nag_tau", 'FLOAT')

class WanVideoNAGOutputs(OutputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')

class WanVideoNAG(Node[WanVideoNAGInputs, WanVideoNAGOutputs]):
    """
    Original name: WanVideoNAG
    Category: KJNodes/experimental
    https://github.com/ChenDarYen/Normalized-Attention-Guidance

    Inputs:
        - model (Model)
        - conditioning (Conditioning)
        - nag_scale (float) (default: 11.0)
          Strength of negative guidance effect
        - nag_alpha (float) (default: 0.25)
          Mixing coefficient in that controls the balance between the normalized guided representation and the original positive representation.
        - nag_tau (float) (default: 2.5)
          Clipping threshold that controls how much the guided attention can deviate from the positive attention.

    Outputs:
        - model (Model)
    """
    _original_name: str = 'WanVideoNAG'

    def __init__(self, model: Slot[Model], conditioning: Slot[Conditioning], nag_scale: float = 11.0, nag_alpha: float = 0.25, nag_tau: float = 2.5):
        super().__init__(**{"model": model, "conditioning": conditioning, "nag_scale": nag_scale, "nag_alpha": nag_alpha, "nag_tau": nag_tau})
        self.inputs = WanVideoNAGInputs(self)
        self.outputs = WanVideoNAGOutputs(self)

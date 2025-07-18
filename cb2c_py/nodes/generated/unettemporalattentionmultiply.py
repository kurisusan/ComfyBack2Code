
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for UNetTemporalAttentionMultiply
class UNetTemporalAttentionMultiplyInputs(InputSlots):
    model: Slot[Model]
    self_structural: Slot[float]
    self_temporal: Slot[float]
    cross_structural: Slot[float]
    cross_temporal: Slot[float]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')
        self.self_structural = Slot[float](node, "self_structural", 'FLOAT')
        self.self_temporal = Slot[float](node, "self_temporal", 'FLOAT')
        self.cross_structural = Slot[float](node, "cross_structural", 'FLOAT')
        self.cross_temporal = Slot[float](node, "cross_temporal", 'FLOAT')

class UNetTemporalAttentionMultiplyOutputs(OutputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "MODEL", 'MODEL')

class UNetTemporalAttentionMultiply(Node[UNetTemporalAttentionMultiplyInputs, UNetTemporalAttentionMultiplyOutputs]):
    """
    Original name: UNetTemporalAttentionMultiply
    Category: _for_testing/attention_experiments
    

    Inputs:
        - model (Model)
        - self_structural (float) (default: 1.0)
        - self_temporal (float) (default: 1.0)
        - cross_structural (float) (default: 1.0)
        - cross_temporal (float) (default: 1.0)

    Outputs:
        - model (Model)
    """
    _original_name: str = 'UNetTemporalAttentionMultiply'

    def __init__(self, model: Slot[Model], self_structural: float = 1.0, self_temporal: float = 1.0, cross_structural: float = 1.0, cross_temporal: float = 1.0):
        super().__init__(**{"model": model, "self_structural": self_structural, "self_temporal": self_temporal, "cross_structural": cross_structural, "cross_temporal": cross_temporal})
        self.inputs = UNetTemporalAttentionMultiplyInputs(self)
        self.outputs = UNetTemporalAttentionMultiplyOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SplitSigmas
class SplitSigmasInputs(InputSlots):
    sigmas: Slot[Any]
    step: Slot[int]
    def __init__(self, node: "Node"):
        self.sigmas = Slot[Any](node, "sigmas", 'SIGMAS')
        self.step = Slot[int](node, "step", 'INT')

class SplitSigmasOutputs(OutputSlots):
    high_sigmas: Slot[Any]
    low_sigmas: Slot[Any]
    def __init__(self, node: "Node"):
        self.high_sigmas = Slot[Any](node, "high_sigmas", 'SIGMAS')
        self.low_sigmas = Slot[Any](node, "low_sigmas", 'SIGMAS')

class SplitSigmas(Node[SplitSigmasInputs, SplitSigmasOutputs]):
    """
    Original name: SplitSigmas
    Category: sampling/custom_sampling/sigmas
    

    Inputs:
        - sigmas (Any)
        - step (int) (default: 0)

    Outputs:
        - high_sigmas (Any)
        - low_sigmas (Any)
    """
    _original_name: str = 'SplitSigmas'

    def __init__(self, sigmas: Slot[Any], step: int = 0):
        super().__init__(**{"sigmas": sigmas, "step": step})
        self.inputs = SplitSigmasInputs(self)
        self.outputs = SplitSigmasOutputs(self)

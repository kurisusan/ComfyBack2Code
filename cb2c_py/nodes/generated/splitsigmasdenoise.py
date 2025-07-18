
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SplitSigmasDenoise
class SplitSigmasDenoiseInputs(InputSlots):
    sigmas: Slot[Any]
    denoise: Slot[float]
    def __init__(self, node: "Node"):
        self.sigmas = Slot[Any](node, "sigmas", 'SIGMAS')
        self.denoise = Slot[float](node, "denoise", 'FLOAT')

class SplitSigmasDenoiseOutputs(OutputSlots):
    high_sigmas: Slot[Any]
    low_sigmas: Slot[Any]
    def __init__(self, node: "Node"):
        self.high_sigmas = Slot[Any](node, "high_sigmas", 'SIGMAS')
        self.low_sigmas = Slot[Any](node, "low_sigmas", 'SIGMAS')

class SplitSigmasDenoise(Node[SplitSigmasDenoiseInputs, SplitSigmasDenoiseOutputs]):
    """
    Original name: SplitSigmasDenoise
    Category: sampling/custom_sampling/sigmas
    

    Inputs:
        - sigmas (Any)
        - denoise (float) (default: 1.0)

    Outputs:
        - high_sigmas (Any)
        - low_sigmas (Any)
    """
    _original_name: str = 'SplitSigmasDenoise'

    def __init__(self, sigmas: Slot[Any], denoise: float = 1.0):
        super().__init__(**{"sigmas": sigmas, "denoise": denoise})
        self.inputs = SplitSigmasDenoiseInputs(self)
        self.outputs = SplitSigmasDenoiseOutputs(self)

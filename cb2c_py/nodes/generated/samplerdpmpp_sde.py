
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SamplerDPMPP_SDE
class SamplerDPMPP_SDEInputs(InputSlots):
    eta: Slot[float]
    s_noise: Slot[float]
    r: Slot[float]
    noise_device: Slot[str]
    def __init__(self, node: "Node"):
        self.eta = Slot[float](node, "eta", 'FLOAT')
        self.s_noise = Slot[float](node, "s_noise", 'FLOAT')
        self.r = Slot[float](node, "r", 'FLOAT')
        self.noise_device = Slot[str](node, "noise_device", ['gpu', 'cpu'])

class SamplerDPMPP_SDEOutputs(OutputSlots):
    sampler: Slot[Any]
    def __init__(self, node: "Node"):
        self.sampler = Slot[Any](node, "SAMPLER", 'SAMPLER')

class SamplerDPMPP_SDE(Node[SamplerDPMPP_SDEInputs, SamplerDPMPP_SDEOutputs]):
    """
    Original name: SamplerDPMPP_SDE
    Category: sampling/custom_sampling/samplers
    

    Inputs:
        - eta (float) (default: 1.0)
        - s_noise (float) (default: 1.0)
        - r (float) (default: 0.5)
        - noise_device (str)

    Outputs:
        - sampler (Any)
    """
    _original_name: str = 'SamplerDPMPP_SDE'

    def __init__(self, noise_device: str, eta: float = 1.0, s_noise: float = 1.0, r: float = 0.5):
        super().__init__(**{"eta": eta, "s_noise": s_noise, "r": r, "noise_device": noise_device})
        self.inputs = SamplerDPMPP_SDEInputs(self)
        self.outputs = SamplerDPMPP_SDEOutputs(self)

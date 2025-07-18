
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SamplerDPMPP_2M_SDE
class SamplerDPMPP_2M_SDEInputs(InputSlots):
    solver_type: Slot[str]
    eta: Slot[float]
    s_noise: Slot[float]
    noise_device: Slot[str]
    def __init__(self, node: "Node"):
        self.solver_type = Slot[str](node, "solver_type", ['midpoint', 'heun'])
        self.eta = Slot[float](node, "eta", 'FLOAT')
        self.s_noise = Slot[float](node, "s_noise", 'FLOAT')
        self.noise_device = Slot[str](node, "noise_device", ['gpu', 'cpu'])

class SamplerDPMPP_2M_SDEOutputs(OutputSlots):
    sampler: Slot[Any]
    def __init__(self, node: "Node"):
        self.sampler = Slot[Any](node, "SAMPLER", 'SAMPLER')

class SamplerDPMPP_2M_SDE(Node[SamplerDPMPP_2M_SDEInputs, SamplerDPMPP_2M_SDEOutputs]):
    """
    Original name: SamplerDPMPP_2M_SDE
    Category: sampling/custom_sampling/samplers
    

    Inputs:
        - solver_type (str)
        - eta (float) (default: 1.0)
        - s_noise (float) (default: 1.0)
        - noise_device (str)

    Outputs:
        - sampler (Any)
    """
    _original_name: str = 'SamplerDPMPP_2M_SDE'

    def __init__(self, solver_type: str, noise_device: str, eta: float = 1.0, s_noise: float = 1.0):
        super().__init__(**{"solver_type": solver_type, "eta": eta, "s_noise": s_noise, "noise_device": noise_device})
        self.inputs = SamplerDPMPP_2M_SDEInputs(self)
        self.outputs = SamplerDPMPP_2M_SDEOutputs(self)

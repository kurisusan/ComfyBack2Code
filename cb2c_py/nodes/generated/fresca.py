
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for FreSca
class FreScaInputs(InputSlots):
    model: Slot[Model]
    scale_low: Slot[float]
    scale_high: Slot[float]
    freq_cutoff: Slot[int]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')
        self.scale_low = Slot[float](node, "scale_low", 'FLOAT')
        self.scale_high = Slot[float](node, "scale_high", 'FLOAT')
        self.freq_cutoff = Slot[int](node, "freq_cutoff", 'INT')

class FreScaOutputs(OutputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "MODEL", 'MODEL')

class FreSca(Node[FreScaInputs, FreScaOutputs]):
    """
    Original name: FreSca
    Category: _for_testing
    Applies frequency-dependent scaling to the guidance

    Inputs:
        - model (Model)
        - scale_low (float) (default: 1.0)
          Scaling factor for low-frequency components
        - scale_high (float) (default: 1.25)
          Scaling factor for high-frequency components
        - freq_cutoff (int) (default: 20)
          Number of frequency indices around center to consider as low-frequency

    Outputs:
        - model (Model)
    """
    _original_name: str = 'FreSca'

    def __init__(self, model: Slot[Model], scale_low: float = 1.0, scale_high: float = 1.25, freq_cutoff: int = 20):
        super().__init__(**{"model": model, "scale_low": scale_low, "scale_high": scale_high, "freq_cutoff": freq_cutoff})
        self.inputs = FreScaInputs(self)
        self.outputs = FreScaOutputs(self)

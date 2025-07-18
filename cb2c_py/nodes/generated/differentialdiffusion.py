
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for DifferentialDiffusion
class DifferentialDiffusionInputs(InputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')

class DifferentialDiffusionOutputs(OutputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "MODEL", 'MODEL')

class DifferentialDiffusion(Node[DifferentialDiffusionInputs, DifferentialDiffusionOutputs]):
    """
    Original name: DifferentialDiffusion
    Category: _for_testing
    

    Inputs:
        - model (Model)

    Outputs:
        - model (Model)
    """
    _original_name: str = 'DifferentialDiffusion'

    def __init__(self, model: Slot[Model]):
        super().__init__(**{"model": model})
        self.inputs = DifferentialDiffusionInputs(self)
        self.outputs = DifferentialDiffusionOutputs(self)

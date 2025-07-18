
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for Mahiro
class MahiroInputs(InputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')

class MahiroOutputs(OutputSlots):
    patched_model: Slot[Model]
    def __init__(self, node: "Node"):
        self.patched_model = Slot[Model](node, "patched_model", 'MODEL')

class Mahiro(Node[MahiroInputs, MahiroOutputs]):
    """
    Original name: Mahiro
    Category: _for_testing
    Modify the guidance to scale more on the 'direction' of the positive prompt rather than the difference between the negative prompt.

    Inputs:
        - model (Model)

    Outputs:
        - patched_model (Model)
    """
    _original_name: str = 'Mahiro'

    def __init__(self, model: Slot[Model]):
        super().__init__(**{"model": model})
        self.inputs = MahiroInputs(self)
        self.outputs = MahiroOutputs(self)

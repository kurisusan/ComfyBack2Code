
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for PreviewAny
class PreviewAnyInputs(InputSlots):
    source: Slot[Any]
    def __init__(self, node: "Node"):
        self.source = Slot[Any](node, "source", '*')

class PreviewAnyOutputs(OutputSlots):

    def __init__(self, node: "Node"):
        pass

class PreviewAny(Node[PreviewAnyInputs, PreviewAnyOutputs]):
    """
    Original name: PreviewAny
    Category: utils
    

    Inputs:
        - source (Any)

    Outputs:
        No outputs.
    """
    _original_name: str = 'PreviewAny'

    def __init__(self, source: Slot[Any]):
        super().__init__(**{"source": source})
        self.inputs = PreviewAnyInputs(self)
        self.outputs = PreviewAnyOutputs(self)

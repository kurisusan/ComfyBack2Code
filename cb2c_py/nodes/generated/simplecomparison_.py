
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SimpleComparison_
class SimpleComparison_Inputs(InputSlots):
    a: Slot[Any]
    b: Slot[Any]
    comparison: Slot[str]
    def __init__(self, node: "Node"):
        self.a = Slot[Any](node, "a", '*')
        self.b = Slot[Any](node, "b", '*')
        self.comparison = Slot[str](node, "comparison", ['==', '!=', '<', '<=', '>', '>='])

class SimpleComparison_Outputs(OutputSlots):
    boolean: Slot[bool]
    def __init__(self, node: "Node"):
        self.boolean = Slot[bool](node, "BOOLEAN", 'BOOLEAN')

class SimpleComparison_(Node[SimpleComparison_Inputs, SimpleComparison_Outputs]):
    """
    Original name: SimpleComparison+
    Category: essentials/utilities
    

    Inputs:
        - a (Any) (default: 0)
        - b (Any) (default: 0)
        - comparison (str)

    Outputs:
        - boolean (bool)
    """
    _original_name: str = 'SimpleComparison+'

    def __init__(self, comparison: str, a: Slot[Any] = 0, b: Slot[Any] = 0):
        super().__init__(**{"a": a, "b": b, "comparison": comparison})
        self.inputs = SimpleComparison_Inputs(self)
        self.outputs = SimpleComparison_Outputs(self)

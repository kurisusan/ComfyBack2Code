
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for CFGGuider
class CFGGuiderInputs(InputSlots):
    model: Slot[Model]
    positive: Slot[Conditioning]
    negative: Slot[Conditioning]
    cfg: Slot[float]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')
        self.positive = Slot[Conditioning](node, "positive", 'CONDITIONING')
        self.negative = Slot[Conditioning](node, "negative", 'CONDITIONING')
        self.cfg = Slot[float](node, "cfg", 'FLOAT')

class CFGGuiderOutputs(OutputSlots):
    guider: Slot[Any]
    def __init__(self, node: "Node"):
        self.guider = Slot[Any](node, "GUIDER", 'GUIDER')

class CFGGuider(Node[CFGGuiderInputs, CFGGuiderOutputs]):
    """
    Original name: CFGGuider
    Category: sampling/custom_sampling/guiders
    

    Inputs:
        - model (Model)
        - positive (Conditioning)
        - negative (Conditioning)
        - cfg (float) (default: 8.0)

    Outputs:
        - guider (Any)
    """
    _original_name: str = 'CFGGuider'

    def __init__(self, model: Slot[Model], positive: Slot[Conditioning], negative: Slot[Conditioning], cfg: float = 8.0):
        super().__init__(**{"model": model, "positive": positive, "negative": negative, "cfg": cfg})
        self.inputs = CFGGuiderInputs(self)
        self.outputs = CFGGuiderOutputs(self)

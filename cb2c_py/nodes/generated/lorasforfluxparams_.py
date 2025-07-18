
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for LorasForFluxParams_
class LorasForFluxParams_Inputs(InputSlots):
    lora_1: Slot[str]
    strength_model_1: Slot[str]
    def __init__(self, node: "Node"):
        self.lora_1 = Slot[str](node, "lora_1", [])
        self.strength_model_1 = Slot[str](node, "strength_model_1", 'STRING')

class LorasForFluxParams_Outputs(OutputSlots):
    lora_params: Slot[Any]
    def __init__(self, node: "Node"):
        self.lora_params = Slot[Any](node, "LORA_PARAMS", 'LORA_PARAMS')

class LorasForFluxParams_(Node[LorasForFluxParams_Inputs, LorasForFluxParams_Outputs]):
    """
    Original name: LorasForFluxParams+
    Category: essentials/sampling
    

    Inputs:
        - lora_1 (str)
          The name of the LoRA.
        - strength_model_1 (str) (default: '1.0')

    Outputs:
        - lora_params (Any)
    """
    _original_name: str = 'LorasForFluxParams+'

    def __init__(self, lora_1: str, strength_model_1: str = '1.0'):
        super().__init__(**{"lora_1": lora_1, "strength_model_1": strength_model_1})
        self.inputs = LorasForFluxParams_Inputs(self)
        self.outputs = LorasForFluxParams_Outputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SDXL_Power_Prompt___Simple___Negative__rgthree_
class SDXL_Power_Prompt___Simple___Negative__rgthree_Inputs(InputSlots):
    prompt_g: Slot[str]
    prompt_l: Slot[str]
    def __init__(self, node: "Node"):
        self.prompt_g = Slot[str](node, "prompt_g", 'STRING')
        self.prompt_l = Slot[str](node, "prompt_l", 'STRING')

class SDXL_Power_Prompt___Simple___Negative__rgthree_Outputs(OutputSlots):
    conditioning: Slot[Conditioning]
    text_g: Slot[str]
    text_l: Slot[str]
    def __init__(self, node: "Node"):
        self.conditioning = Slot[Conditioning](node, "CONDITIONING", 'CONDITIONING')
        self.text_g = Slot[str](node, "TEXT_G", 'STRING')
        self.text_l = Slot[str](node, "TEXT_L", 'STRING')

class SDXL_Power_Prompt___Simple___Negative__rgthree_(Node[SDXL_Power_Prompt___Simple___Negative__rgthree_Inputs, SDXL_Power_Prompt___Simple___Negative__rgthree_Outputs]):
    """
    Original name: SDXL Power Prompt - Simple / Negative (rgthree)
    Category: rgthree
    

    Inputs:
        - prompt_g (str)
        - prompt_l (str)

    Outputs:
        - conditioning (Conditioning)
        - text_g (str)
        - text_l (str)
    """
    _original_name: str = 'SDXL Power Prompt - Simple / Negative (rgthree)'

    def __init__(self, prompt_g: str, prompt_l: str):
        super().__init__(**{"prompt_g": prompt_g, "prompt_l": prompt_l})
        self.inputs = SDXL_Power_Prompt___Simple___Negative__rgthree_Inputs(self)
        self.outputs = SDXL_Power_Prompt___Simple___Negative__rgthree_Outputs(self)

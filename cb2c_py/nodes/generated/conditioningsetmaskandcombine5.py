
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ConditioningSetMaskAndCombine5
class ConditioningSetMaskAndCombine5Inputs(InputSlots):
    positive_1: Slot[Conditioning]
    negative_1: Slot[Conditioning]
    positive_2: Slot[Conditioning]
    negative_2: Slot[Conditioning]
    positive_3: Slot[Conditioning]
    negative_3: Slot[Conditioning]
    positive_4: Slot[Conditioning]
    negative_4: Slot[Conditioning]
    positive_5: Slot[Conditioning]
    negative_5: Slot[Conditioning]
    mask_1: Slot[Image]
    mask_2: Slot[Image]
    mask_3: Slot[Image]
    mask_4: Slot[Image]
    mask_5: Slot[Image]
    mask_1_strength: Slot[float]
    mask_2_strength: Slot[float]
    mask_3_strength: Slot[float]
    mask_4_strength: Slot[float]
    mask_5_strength: Slot[float]
    set_cond_area: Slot[str]
    def __init__(self, node: "Node"):
        self.positive_1 = Slot[Conditioning](node, "positive_1", 'CONDITIONING')
        self.negative_1 = Slot[Conditioning](node, "negative_1", 'CONDITIONING')
        self.positive_2 = Slot[Conditioning](node, "positive_2", 'CONDITIONING')
        self.negative_2 = Slot[Conditioning](node, "negative_2", 'CONDITIONING')
        self.positive_3 = Slot[Conditioning](node, "positive_3", 'CONDITIONING')
        self.negative_3 = Slot[Conditioning](node, "negative_3", 'CONDITIONING')
        self.positive_4 = Slot[Conditioning](node, "positive_4", 'CONDITIONING')
        self.negative_4 = Slot[Conditioning](node, "negative_4", 'CONDITIONING')
        self.positive_5 = Slot[Conditioning](node, "positive_5", 'CONDITIONING')
        self.negative_5 = Slot[Conditioning](node, "negative_5", 'CONDITIONING')
        self.mask_1 = Slot[Image](node, "mask_1", 'MASK')
        self.mask_2 = Slot[Image](node, "mask_2", 'MASK')
        self.mask_3 = Slot[Image](node, "mask_3", 'MASK')
        self.mask_4 = Slot[Image](node, "mask_4", 'MASK')
        self.mask_5 = Slot[Image](node, "mask_5", 'MASK')
        self.mask_1_strength = Slot[float](node, "mask_1_strength", 'FLOAT')
        self.mask_2_strength = Slot[float](node, "mask_2_strength", 'FLOAT')
        self.mask_3_strength = Slot[float](node, "mask_3_strength", 'FLOAT')
        self.mask_4_strength = Slot[float](node, "mask_4_strength", 'FLOAT')
        self.mask_5_strength = Slot[float](node, "mask_5_strength", 'FLOAT')
        self.set_cond_area = Slot[str](node, "set_cond_area", ['default', 'mask bounds'])

class ConditioningSetMaskAndCombine5Outputs(OutputSlots):
    combined_positive: Slot[Conditioning]
    combined_negative: Slot[Conditioning]
    def __init__(self, node: "Node"):
        self.combined_positive = Slot[Conditioning](node, "combined_positive", 'CONDITIONING')
        self.combined_negative = Slot[Conditioning](node, "combined_negative", 'CONDITIONING')

class ConditioningSetMaskAndCombine5(Node[ConditioningSetMaskAndCombine5Inputs, ConditioningSetMaskAndCombine5Outputs]):
    """
    Original name: ConditioningSetMaskAndCombine5
    Category: KJNodes/masking/conditioning
    
Bundles multiple conditioning mask and combine nodes into one,functionality is identical to ComfyUI native nodes


    Inputs:
        - positive_1 (Conditioning)
        - negative_1 (Conditioning)
        - positive_2 (Conditioning)
        - negative_2 (Conditioning)
        - positive_3 (Conditioning)
        - negative_3 (Conditioning)
        - positive_4 (Conditioning)
        - negative_4 (Conditioning)
        - positive_5 (Conditioning)
        - negative_5 (Conditioning)
        - mask_1 (Image)
        - mask_2 (Image)
        - mask_3 (Image)
        - mask_4 (Image)
        - mask_5 (Image)
        - mask_1_strength (float) (default: 1.0)
        - mask_2_strength (float) (default: 1.0)
        - mask_3_strength (float) (default: 1.0)
        - mask_4_strength (float) (default: 1.0)
        - mask_5_strength (float) (default: 1.0)
        - set_cond_area (str)

    Outputs:
        - combined_positive (Conditioning)
        - combined_negative (Conditioning)
    """
    _original_name: str = 'ConditioningSetMaskAndCombine5'

    def __init__(self, positive_1: Slot[Conditioning], negative_1: Slot[Conditioning], positive_2: Slot[Conditioning], negative_2: Slot[Conditioning], positive_3: Slot[Conditioning], negative_3: Slot[Conditioning], positive_4: Slot[Conditioning], negative_4: Slot[Conditioning], positive_5: Slot[Conditioning], negative_5: Slot[Conditioning], mask_1: Slot[Image], mask_2: Slot[Image], mask_3: Slot[Image], mask_4: Slot[Image], mask_5: Slot[Image], set_cond_area: str, mask_1_strength: float = 1.0, mask_2_strength: float = 1.0, mask_3_strength: float = 1.0, mask_4_strength: float = 1.0, mask_5_strength: float = 1.0):
        super().__init__(**{"positive_1": positive_1, "negative_1": negative_1, "positive_2": positive_2, "negative_2": negative_2, "positive_3": positive_3, "negative_3": negative_3, "positive_4": positive_4, "negative_4": negative_4, "positive_5": positive_5, "negative_5": negative_5, "mask_1": mask_1, "mask_2": mask_2, "mask_3": mask_3, "mask_4": mask_4, "mask_5": mask_5, "mask_1_strength": mask_1_strength, "mask_2_strength": mask_2_strength, "mask_3_strength": mask_3_strength, "mask_4_strength": mask_4_strength, "mask_5_strength": mask_5_strength, "set_cond_area": set_cond_area})
        self.inputs = ConditioningSetMaskAndCombine5Inputs(self)
        self.outputs = ConditioningSetMaskAndCombine5Outputs(self)

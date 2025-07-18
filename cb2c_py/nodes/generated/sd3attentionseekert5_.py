
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for SD3AttentionSeekerT5_
class SD3AttentionSeekerT5_Inputs(InputSlots):
    clip: Slot[Clip]
    apply_to_query: Slot[bool]
    apply_to_key: Slot[bool]
    apply_to_value: Slot[bool]
    apply_to_out: Slot[bool]
    t5xxl_0: Slot[float]
    t5xxl_1: Slot[float]
    t5xxl_2: Slot[float]
    t5xxl_3: Slot[float]
    t5xxl_4: Slot[float]
    t5xxl_5: Slot[float]
    t5xxl_6: Slot[float]
    t5xxl_7: Slot[float]
    t5xxl_8: Slot[float]
    t5xxl_9: Slot[float]
    t5xxl_10: Slot[float]
    t5xxl_11: Slot[float]
    t5xxl_12: Slot[float]
    t5xxl_13: Slot[float]
    t5xxl_14: Slot[float]
    t5xxl_15: Slot[float]
    t5xxl_16: Slot[float]
    t5xxl_17: Slot[float]
    t5xxl_18: Slot[float]
    t5xxl_19: Slot[float]
    t5xxl_20: Slot[float]
    t5xxl_21: Slot[float]
    t5xxl_22: Slot[float]
    t5xxl_23: Slot[float]
    def __init__(self, node: "Node"):
        self.clip = Slot[Clip](node, "clip", 'CLIP')
        self.apply_to_query = Slot[bool](node, "apply_to_query", 'BOOLEAN')
        self.apply_to_key = Slot[bool](node, "apply_to_key", 'BOOLEAN')
        self.apply_to_value = Slot[bool](node, "apply_to_value", 'BOOLEAN')
        self.apply_to_out = Slot[bool](node, "apply_to_out", 'BOOLEAN')
        self.t5xxl_0 = Slot[float](node, "t5xxl_0", 'FLOAT')
        self.t5xxl_1 = Slot[float](node, "t5xxl_1", 'FLOAT')
        self.t5xxl_2 = Slot[float](node, "t5xxl_2", 'FLOAT')
        self.t5xxl_3 = Slot[float](node, "t5xxl_3", 'FLOAT')
        self.t5xxl_4 = Slot[float](node, "t5xxl_4", 'FLOAT')
        self.t5xxl_5 = Slot[float](node, "t5xxl_5", 'FLOAT')
        self.t5xxl_6 = Slot[float](node, "t5xxl_6", 'FLOAT')
        self.t5xxl_7 = Slot[float](node, "t5xxl_7", 'FLOAT')
        self.t5xxl_8 = Slot[float](node, "t5xxl_8", 'FLOAT')
        self.t5xxl_9 = Slot[float](node, "t5xxl_9", 'FLOAT')
        self.t5xxl_10 = Slot[float](node, "t5xxl_10", 'FLOAT')
        self.t5xxl_11 = Slot[float](node, "t5xxl_11", 'FLOAT')
        self.t5xxl_12 = Slot[float](node, "t5xxl_12", 'FLOAT')
        self.t5xxl_13 = Slot[float](node, "t5xxl_13", 'FLOAT')
        self.t5xxl_14 = Slot[float](node, "t5xxl_14", 'FLOAT')
        self.t5xxl_15 = Slot[float](node, "t5xxl_15", 'FLOAT')
        self.t5xxl_16 = Slot[float](node, "t5xxl_16", 'FLOAT')
        self.t5xxl_17 = Slot[float](node, "t5xxl_17", 'FLOAT')
        self.t5xxl_18 = Slot[float](node, "t5xxl_18", 'FLOAT')
        self.t5xxl_19 = Slot[float](node, "t5xxl_19", 'FLOAT')
        self.t5xxl_20 = Slot[float](node, "t5xxl_20", 'FLOAT')
        self.t5xxl_21 = Slot[float](node, "t5xxl_21", 'FLOAT')
        self.t5xxl_22 = Slot[float](node, "t5xxl_22", 'FLOAT')
        self.t5xxl_23 = Slot[float](node, "t5xxl_23", 'FLOAT')

class SD3AttentionSeekerT5_Outputs(OutputSlots):
    clip: Slot[Clip]
    def __init__(self, node: "Node"):
        self.clip = Slot[Clip](node, "CLIP", 'CLIP')

class SD3AttentionSeekerT5_(Node[SD3AttentionSeekerT5_Inputs, SD3AttentionSeekerT5_Outputs]):
    """
    Original name: SD3AttentionSeekerT5+
    Category: essentials/conditioning
    

    Inputs:
        - clip (Clip)
        - apply_to_query (bool) (default: True)
        - apply_to_key (bool) (default: True)
        - apply_to_value (bool) (default: True)
        - apply_to_out (bool) (default: True)
        - t5xxl_0 (float) (default: 1.0)
        - t5xxl_1 (float) (default: 1.0)
        - t5xxl_2 (float) (default: 1.0)
        - t5xxl_3 (float) (default: 1.0)
        - t5xxl_4 (float) (default: 1.0)
        - t5xxl_5 (float) (default: 1.0)
        - t5xxl_6 (float) (default: 1.0)
        - t5xxl_7 (float) (default: 1.0)
        - t5xxl_8 (float) (default: 1.0)
        - t5xxl_9 (float) (default: 1.0)
        - t5xxl_10 (float) (default: 1.0)
        - t5xxl_11 (float) (default: 1.0)
        - t5xxl_12 (float) (default: 1.0)
        - t5xxl_13 (float) (default: 1.0)
        - t5xxl_14 (float) (default: 1.0)
        - t5xxl_15 (float) (default: 1.0)
        - t5xxl_16 (float) (default: 1.0)
        - t5xxl_17 (float) (default: 1.0)
        - t5xxl_18 (float) (default: 1.0)
        - t5xxl_19 (float) (default: 1.0)
        - t5xxl_20 (float) (default: 1.0)
        - t5xxl_21 (float) (default: 1.0)
        - t5xxl_22 (float) (default: 1.0)
        - t5xxl_23 (float) (default: 1.0)

    Outputs:
        - clip (Clip)
    """
    _original_name: str = 'SD3AttentionSeekerT5+'

    def __init__(self, clip: Slot[Clip], apply_to_query: bool = True, apply_to_key: bool = True, apply_to_value: bool = True, apply_to_out: bool = True, t5xxl_0: float = 1.0, t5xxl_1: float = 1.0, t5xxl_2: float = 1.0, t5xxl_3: float = 1.0, t5xxl_4: float = 1.0, t5xxl_5: float = 1.0, t5xxl_6: float = 1.0, t5xxl_7: float = 1.0, t5xxl_8: float = 1.0, t5xxl_9: float = 1.0, t5xxl_10: float = 1.0, t5xxl_11: float = 1.0, t5xxl_12: float = 1.0, t5xxl_13: float = 1.0, t5xxl_14: float = 1.0, t5xxl_15: float = 1.0, t5xxl_16: float = 1.0, t5xxl_17: float = 1.0, t5xxl_18: float = 1.0, t5xxl_19: float = 1.0, t5xxl_20: float = 1.0, t5xxl_21: float = 1.0, t5xxl_22: float = 1.0, t5xxl_23: float = 1.0):
        super().__init__(**{"clip": clip, "apply_to_query": apply_to_query, "apply_to_key": apply_to_key, "apply_to_value": apply_to_value, "apply_to_out": apply_to_out, "t5xxl_0": t5xxl_0, "t5xxl_1": t5xxl_1, "t5xxl_2": t5xxl_2, "t5xxl_3": t5xxl_3, "t5xxl_4": t5xxl_4, "t5xxl_5": t5xxl_5, "t5xxl_6": t5xxl_6, "t5xxl_7": t5xxl_7, "t5xxl_8": t5xxl_8, "t5xxl_9": t5xxl_9, "t5xxl_10": t5xxl_10, "t5xxl_11": t5xxl_11, "t5xxl_12": t5xxl_12, "t5xxl_13": t5xxl_13, "t5xxl_14": t5xxl_14, "t5xxl_15": t5xxl_15, "t5xxl_16": t5xxl_16, "t5xxl_17": t5xxl_17, "t5xxl_18": t5xxl_18, "t5xxl_19": t5xxl_19, "t5xxl_20": t5xxl_20, "t5xxl_21": t5xxl_21, "t5xxl_22": t5xxl_22, "t5xxl_23": t5xxl_23})
        self.inputs = SD3AttentionSeekerT5_Inputs(self)
        self.outputs = SD3AttentionSeekerT5_Outputs(self)

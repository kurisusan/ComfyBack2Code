
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for WeightScheduleExtend
class WeightScheduleExtendInputs(InputSlots):
    input_values_1: Slot[float]
    input_values_2: Slot[float]
    output_type: Slot[str]
    def __init__(self, node: "Node"):
        self.input_values_1 = Slot[float](node, "input_values_1", 'FLOAT')
        self.input_values_2 = Slot[float](node, "input_values_2", 'FLOAT')
        self.output_type = Slot[str](node, "output_type", ['match_input', 'list', 'pandas series', 'tensor'])

class WeightScheduleExtendOutputs(OutputSlots):
    float: Slot[float]
    def __init__(self, node: "Node"):
        self.float = Slot[float](node, "FLOAT", 'FLOAT')

class WeightScheduleExtend(Node[WeightScheduleExtendInputs, WeightScheduleExtendOutputs]):
    """
    Original name: WeightScheduleExtend
    Category: KJNodes/weights
    
Extends, and converts if needed, different value lists/series  


    Inputs:
        - input_values_1 (float) (default: 0.0)
        - input_values_2 (float) (default: 0.0)
        - output_type (str) (default: 'match_input')

    Outputs:
        - float (float)
    """
    _original_name: str = 'WeightScheduleExtend'

    def __init__(self, input_values_1: float = 0.0, input_values_2: float = 0.0, output_type: str = 'match_input'):
        super().__init__(**{"input_values_1": input_values_1, "input_values_2": input_values_2, "output_type": output_type})
        self.inputs = WeightScheduleExtendInputs(self)
        self.outputs = WeightScheduleExtendOutputs(self)

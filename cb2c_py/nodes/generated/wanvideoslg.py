
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for WanVideoSLG
class WanVideoSLGInputs(InputSlots):
    blocks: Slot[str]
    start_percent: Slot[float]
    end_percent: Slot[float]
    def __init__(self, node: "Node"):
        self.blocks = Slot[str](node, "blocks", 'STRING')
        self.start_percent = Slot[float](node, "start_percent", 'FLOAT')
        self.end_percent = Slot[float](node, "end_percent", 'FLOAT')

class WanVideoSLGOutputs(OutputSlots):
    slg_args: Slot[Any]
    def __init__(self, node: "Node"):
        self.slg_args = Slot[Any](node, "slg_args", 'SLGARGS')

class WanVideoSLG(Node[WanVideoSLGInputs, WanVideoSLGOutputs]):
    """
    Original name: WanVideoSLG
    Category: WanVideoWrapper
    Skips uncond on the selected blocks

    Inputs:
        - blocks (str) (default: '10')
          Blocks to skip uncond on, separated by comma, index starts from 0
        - start_percent (float) (default: 0.1)
          Start percent of the control signal
        - end_percent (float) (default: 1.0)
          End percent of the control signal

    Outputs:
        - slg_args (Any)
    """
    _original_name: str = 'WanVideoSLG'

    def __init__(self, blocks: str = '10', start_percent: float = 0.1, end_percent: float = 1.0):
        super().__init__(**{"blocks": blocks, "start_percent": start_percent, "end_percent": end_percent})
        self.inputs = WanVideoSLGInputs(self)
        self.outputs = WanVideoSLGOutputs(self)

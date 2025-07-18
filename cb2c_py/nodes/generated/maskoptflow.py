
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for MaskOptFlow
class MaskOptFlowInputs(InputSlots):
    optical_flow: Slot[Any]
    mask: Slot[Image]
    def __init__(self, node: "Node"):
        self.optical_flow = Slot[Any](node, "optical_flow", 'OPTICAL_FLOW')
        self.mask = Slot[Image](node, "mask", 'MASK')

class MaskOptFlowOutputs(OutputSlots):
    optical_flow: Slot[Any]
    preview_image: Slot[Image]
    def __init__(self, node: "Node"):
        self.optical_flow = Slot[Any](node, "OPTICAL_FLOW", 'OPTICAL_FLOW')
        self.preview_image = Slot[Image](node, "PREVIEW_IMAGE", 'IMAGE')

class MaskOptFlow(Node[MaskOptFlowInputs, MaskOptFlowOutputs]):
    """
    Original name: MaskOptFlow
    Category: ControlNet Preprocessors/Optical Flow
    

    Inputs:
        - optical_flow (Any)
        - mask (Image)

    Outputs:
        - optical_flow (Any)
        - preview_image (Image)
    """
    _original_name: str = 'MaskOptFlow'

    def __init__(self, optical_flow: Slot[Any], mask: Slot[Image]):
        super().__init__(**{"optical_flow": optical_flow, "mask": mask})
        self.inputs = MaskOptFlowInputs(self)
        self.outputs = MaskOptFlowOutputs(self)

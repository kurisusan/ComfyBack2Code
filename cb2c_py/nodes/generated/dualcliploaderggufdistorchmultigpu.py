
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for DualCLIPLoaderGGUFDisTorchMultiGPU
class DualCLIPLoaderGGUFDisTorchMultiGPUInputs(InputSlots):
    clip_name1: Slot[str]
    clip_name2: Slot[str]
    type: Slot[str]
    def __init__(self, node: "Node"):
        self.clip_name1 = Slot[str](node, "clip_name1", ['umt5_xxl_fp8_e4m3fn_scaled.safetensors'])
        self.clip_name2 = Slot[str](node, "clip_name2", ['umt5_xxl_fp8_e4m3fn_scaled.safetensors'])
        self.type = Slot[str](node, "type", ['sdxl', 'sd3', 'flux', 'hunyuan_video'])

class DualCLIPLoaderGGUFDisTorchMultiGPUOutputs(OutputSlots):
    clip: Slot[Clip]
    def __init__(self, node: "Node"):
        self.clip = Slot[Clip](node, "CLIP", 'CLIP')

class DualCLIPLoaderGGUFDisTorchMultiGPU(Node[DualCLIPLoaderGGUFDisTorchMultiGPUInputs, DualCLIPLoaderGGUFDisTorchMultiGPUOutputs]):
    """
    Original name: DualCLIPLoaderGGUFDisTorchMultiGPU
    Category: multigpu
    

    Inputs:
        - clip_name1 (str)
        - clip_name2 (str)
        - type (str)

    Outputs:
        - clip (Clip)
    """
    _original_name: str = 'DualCLIPLoaderGGUFDisTorchMultiGPU'

    def __init__(self, clip_name1: str, clip_name2: str, type: str):
        super().__init__(**{"clip_name1": clip_name1, "clip_name2": clip_name2, "type": type})
        self.inputs = DualCLIPLoaderGGUFDisTorchMultiGPUInputs(self)
        self.outputs = DualCLIPLoaderGGUFDisTorchMultiGPUOutputs(self)

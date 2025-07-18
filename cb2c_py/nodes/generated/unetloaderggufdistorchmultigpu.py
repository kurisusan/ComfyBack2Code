
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for UnetLoaderGGUFDisTorchMultiGPU
class UnetLoaderGGUFDisTorchMultiGPUInputs(InputSlots):
    unet_name: Slot[str]
    def __init__(self, node: "Node"):
        self.unet_name = Slot[str](node, "unet_name", ['wan2.1-t2v-14b-Q4_K_M.gguf'])

class UnetLoaderGGUFDisTorchMultiGPUOutputs(OutputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "MODEL", 'MODEL')

class UnetLoaderGGUFDisTorchMultiGPU(Node[UnetLoaderGGUFDisTorchMultiGPUInputs, UnetLoaderGGUFDisTorchMultiGPUOutputs]):
    """
    Original name: UnetLoaderGGUFDisTorchMultiGPU
    Category: multigpu
    

    Inputs:
        - unet_name (str)

    Outputs:
        - model (Model)
    """
    _original_name: str = 'UnetLoaderGGUFDisTorchMultiGPU'

    def __init__(self, unet_name: str):
        super().__init__(**{"unet_name": unet_name})
        self.inputs = UnetLoaderGGUFDisTorchMultiGPUInputs(self)
        self.outputs = UnetLoaderGGUFDisTorchMultiGPUOutputs(self)

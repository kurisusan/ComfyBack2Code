
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for TorchCompileControlNet
class TorchCompileControlNetInputs(InputSlots):
    controlnet: Slot[Any]
    backend: Slot[str]
    fullgraph: Slot[bool]
    mode: Slot[str]
    def __init__(self, node: "Node"):
        self.controlnet = Slot[Any](node, "controlnet", 'CONTROL_NET')
        self.backend = Slot[str](node, "backend", ['inductor', 'cudagraphs'])
        self.fullgraph = Slot[bool](node, "fullgraph", 'BOOLEAN')
        self.mode = Slot[str](node, "mode", ['default', 'max-autotune', 'max-autotune-no-cudagraphs', 'reduce-overhead'])

class TorchCompileControlNetOutputs(OutputSlots):
    control_net: Slot[Any]
    def __init__(self, node: "Node"):
        self.control_net = Slot[Any](node, "CONTROL_NET", 'CONTROL_NET')

class TorchCompileControlNet(Node[TorchCompileControlNetInputs, TorchCompileControlNetOutputs]):
    """
    Original name: TorchCompileControlNet
    Category: KJNodes/torchcompile
    

    Inputs:
        - controlnet (Any)
        - backend (str)
        - fullgraph (bool) (default: False)
          Enable full graph mode
        - mode (str) (default: 'default')

    Outputs:
        - control_net (Any)
    """
    _original_name: str = 'TorchCompileControlNet'

    def __init__(self, controlnet: Slot[Any], backend: str, fullgraph: bool = False, mode: str = 'default'):
        super().__init__(**{"controlnet": controlnet, "backend": backend, "fullgraph": fullgraph, "mode": mode})
        self.inputs = TorchCompileControlNetInputs(self)
        self.outputs = TorchCompileControlNetOutputs(self)

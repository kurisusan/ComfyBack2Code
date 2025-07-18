
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for NunchakuWheelInstaller
class NunchakuWheelInstallerInputs(InputSlots):
    source: Slot[str]
    version: Slot[str]
    def __init__(self, node: "Node"):
        self.source = Slot[str](node, "source", ['GitHub Release', 'HuggingFace', 'ModelScope'])
        self.version = Slot[str](node, "version", ['v0.3.1'])

class NunchakuWheelInstallerOutputs(OutputSlots):
    status: Slot[str]
    def __init__(self, node: "Node"):
        self.status = Slot[str](node, "status", 'STRING')

class NunchakuWheelInstaller(Node[NunchakuWheelInstallerInputs, NunchakuWheelInstallerOutputs]):
    """
    Original name: NunchakuWheelInstaller
    Category: Nunchaku
    

    Inputs:
        - source (str)
          Source for downloading nunchaku wheels.
        - version (str)
          Specific version to install.

    Outputs:
        - status (str)
    """
    _original_name: str = 'NunchakuWheelInstaller'

    def __init__(self, source: str, version: str):
        super().__init__(**{"source": source, "version": version})
        self.inputs = NunchakuWheelInstallerInputs(self)
        self.outputs = NunchakuWheelInstallerOutputs(self)

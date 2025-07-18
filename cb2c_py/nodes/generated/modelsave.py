
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ModelSave
class ModelSaveInputs(InputSlots):
    model: Slot[Model]
    filename_prefix: Slot[str]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')
        self.filename_prefix = Slot[str](node, "filename_prefix", 'STRING')

class ModelSaveOutputs(OutputSlots):

    def __init__(self, node: "Node"):
        pass

class ModelSave(Node[ModelSaveInputs, ModelSaveOutputs]):
    """
    Original name: ModelSave
    Category: advanced/model_merging
    

    Inputs:
        - model (Model)
        - filename_prefix (str) (default: 'diffusion_models/ComfyUI')

    Outputs:
        No outputs.
    """
    _original_name: str = 'ModelSave'

    def __init__(self, model: Slot[Model], filename_prefix: str = 'diffusion_models/ComfyUI'):
        super().__init__(**{"model": model, "filename_prefix": filename_prefix})
        self.inputs = ModelSaveInputs(self)
        self.outputs = ModelSaveOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ModelMergeSDXL
class ModelMergeSDXLInputs(InputSlots):
    model1: Slot[Model]
    model2: Slot[Model]
    time_embed_: Slot[float]
    label_emb_: Slot[float]
    input_blocks_0: Slot[float]
    input_blocks_1: Slot[float]
    input_blocks_2: Slot[float]
    input_blocks_3: Slot[float]
    input_blocks_4: Slot[float]
    input_blocks_5: Slot[float]
    input_blocks_6: Slot[float]
    input_blocks_7: Slot[float]
    input_blocks_8: Slot[float]
    middle_block_0: Slot[float]
    middle_block_1: Slot[float]
    middle_block_2: Slot[float]
    output_blocks_0: Slot[float]
    output_blocks_1: Slot[float]
    output_blocks_2: Slot[float]
    output_blocks_3: Slot[float]
    output_blocks_4: Slot[float]
    output_blocks_5: Slot[float]
    output_blocks_6: Slot[float]
    output_blocks_7: Slot[float]
    output_blocks_8: Slot[float]
    out_: Slot[float]
    def __init__(self, node: "Node"):
        self.model1 = Slot[Model](node, "model1", 'MODEL')
        self.model2 = Slot[Model](node, "model2", 'MODEL')
        self.time_embed_ = Slot[float](node, "time_embed_", 'FLOAT')
        self.label_emb_ = Slot[float](node, "label_emb_", 'FLOAT')
        self.input_blocks_0 = Slot[float](node, "input_blocks_0", 'FLOAT')
        self.input_blocks_1 = Slot[float](node, "input_blocks_1", 'FLOAT')
        self.input_blocks_2 = Slot[float](node, "input_blocks_2", 'FLOAT')
        self.input_blocks_3 = Slot[float](node, "input_blocks_3", 'FLOAT')
        self.input_blocks_4 = Slot[float](node, "input_blocks_4", 'FLOAT')
        self.input_blocks_5 = Slot[float](node, "input_blocks_5", 'FLOAT')
        self.input_blocks_6 = Slot[float](node, "input_blocks_6", 'FLOAT')
        self.input_blocks_7 = Slot[float](node, "input_blocks_7", 'FLOAT')
        self.input_blocks_8 = Slot[float](node, "input_blocks_8", 'FLOAT')
        self.middle_block_0 = Slot[float](node, "middle_block_0", 'FLOAT')
        self.middle_block_1 = Slot[float](node, "middle_block_1", 'FLOAT')
        self.middle_block_2 = Slot[float](node, "middle_block_2", 'FLOAT')
        self.output_blocks_0 = Slot[float](node, "output_blocks_0", 'FLOAT')
        self.output_blocks_1 = Slot[float](node, "output_blocks_1", 'FLOAT')
        self.output_blocks_2 = Slot[float](node, "output_blocks_2", 'FLOAT')
        self.output_blocks_3 = Slot[float](node, "output_blocks_3", 'FLOAT')
        self.output_blocks_4 = Slot[float](node, "output_blocks_4", 'FLOAT')
        self.output_blocks_5 = Slot[float](node, "output_blocks_5", 'FLOAT')
        self.output_blocks_6 = Slot[float](node, "output_blocks_6", 'FLOAT')
        self.output_blocks_7 = Slot[float](node, "output_blocks_7", 'FLOAT')
        self.output_blocks_8 = Slot[float](node, "output_blocks_8", 'FLOAT')
        self.out_ = Slot[float](node, "out_", 'FLOAT')

class ModelMergeSDXLOutputs(OutputSlots):
    model: Slot[Model]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "MODEL", 'MODEL')

class ModelMergeSDXL(Node[ModelMergeSDXLInputs, ModelMergeSDXLOutputs]):
    """
    Original name: ModelMergeSDXL
    Category: advanced/model_merging/model_specific
    

    Inputs:
        - model1 (Model)
        - model2 (Model)
        - time_embed_ (float) (default: 1.0)
        - label_emb_ (float) (default: 1.0)
        - input_blocks_0 (float) (default: 1.0)
        - input_blocks_1 (float) (default: 1.0)
        - input_blocks_2 (float) (default: 1.0)
        - input_blocks_3 (float) (default: 1.0)
        - input_blocks_4 (float) (default: 1.0)
        - input_blocks_5 (float) (default: 1.0)
        - input_blocks_6 (float) (default: 1.0)
        - input_blocks_7 (float) (default: 1.0)
        - input_blocks_8 (float) (default: 1.0)
        - middle_block_0 (float) (default: 1.0)
        - middle_block_1 (float) (default: 1.0)
        - middle_block_2 (float) (default: 1.0)
        - output_blocks_0 (float) (default: 1.0)
        - output_blocks_1 (float) (default: 1.0)
        - output_blocks_2 (float) (default: 1.0)
        - output_blocks_3 (float) (default: 1.0)
        - output_blocks_4 (float) (default: 1.0)
        - output_blocks_5 (float) (default: 1.0)
        - output_blocks_6 (float) (default: 1.0)
        - output_blocks_7 (float) (default: 1.0)
        - output_blocks_8 (float) (default: 1.0)
        - out_ (float) (default: 1.0)

    Outputs:
        - model (Model)
    """
    _original_name: str = 'ModelMergeSDXL'

    def __init__(self, model1: Slot[Model], model2: Slot[Model], time_embed_: float = 1.0, label_emb_: float = 1.0, input_blocks_0: float = 1.0, input_blocks_1: float = 1.0, input_blocks_2: float = 1.0, input_blocks_3: float = 1.0, input_blocks_4: float = 1.0, input_blocks_5: float = 1.0, input_blocks_6: float = 1.0, input_blocks_7: float = 1.0, input_blocks_8: float = 1.0, middle_block_0: float = 1.0, middle_block_1: float = 1.0, middle_block_2: float = 1.0, output_blocks_0: float = 1.0, output_blocks_1: float = 1.0, output_blocks_2: float = 1.0, output_blocks_3: float = 1.0, output_blocks_4: float = 1.0, output_blocks_5: float = 1.0, output_blocks_6: float = 1.0, output_blocks_7: float = 1.0, output_blocks_8: float = 1.0, out_: float = 1.0):
        super().__init__(**{"model1": model1, "model2": model2, "time_embed.": time_embed_, "label_emb.": label_emb_, "input_blocks.0": input_blocks_0, "input_blocks.1": input_blocks_1, "input_blocks.2": input_blocks_2, "input_blocks.3": input_blocks_3, "input_blocks.4": input_blocks_4, "input_blocks.5": input_blocks_5, "input_blocks.6": input_blocks_6, "input_blocks.7": input_blocks_7, "input_blocks.8": input_blocks_8, "middle_block.0": middle_block_0, "middle_block.1": middle_block_1, "middle_block.2": middle_block_2, "output_blocks.0": output_blocks_0, "output_blocks.1": output_blocks_1, "output_blocks.2": output_blocks_2, "output_blocks.3": output_blocks_3, "output_blocks.4": output_blocks_4, "output_blocks.5": output_blocks_5, "output_blocks.6": output_blocks_6, "output_blocks.7": output_blocks_7, "output_blocks.8": output_blocks_8, "out.": out_})
        self.inputs = ModelMergeSDXLInputs(self)
        self.outputs = ModelMergeSDXLOutputs(self)

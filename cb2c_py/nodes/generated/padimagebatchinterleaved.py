
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for PadImageBatchInterleaved
class PadImageBatchInterleavedInputs(InputSlots):
    images: Slot[Image]
    empty_frames_per_image: Slot[int]
    pad_frame_value: Slot[float]
    add_after_last: Slot[bool]
    def __init__(self, node: "Node"):
        self.images = Slot[Image](node, "images", 'IMAGE')
        self.empty_frames_per_image = Slot[int](node, "empty_frames_per_image", 'INT')
        self.pad_frame_value = Slot[float](node, "pad_frame_value", 'FLOAT')
        self.add_after_last = Slot[bool](node, "add_after_last", 'BOOLEAN')

class PadImageBatchInterleavedOutputs(OutputSlots):
    images: Slot[Image]
    masks: Slot[Image]
    def __init__(self, node: "Node"):
        self.images = Slot[Image](node, "images", 'IMAGE')
        self.masks = Slot[Image](node, "masks", 'MASK')

class PadImageBatchInterleaved(Node[PadImageBatchInterleavedInputs, PadImageBatchInterleavedOutputs]):
    """
    Original name: PadImageBatchInterleaved
    Category: KJNodes/image
    
Inserts empty frames between the images in a batch.


    Inputs:
        - images (Image)
        - empty_frames_per_image (int) (default: 1)
        - pad_frame_value (float) (default: 0.0)
        - add_after_last (bool) (default: False)

    Outputs:
        - images (Image)
        - masks (Image)
    """
    _original_name: str = 'PadImageBatchInterleaved'

    def __init__(self, images: Slot[Image], empty_frames_per_image: int = 1, pad_frame_value: float = 0.0, add_after_last: bool = False):
        super().__init__(**{"images": images, "empty_frames_per_image": empty_frames_per_image, "pad_frame_value": pad_frame_value, "add_after_last": add_after_last})
        self.inputs = PadImageBatchInterleavedInputs(self)
        self.outputs = PadImageBatchInterleavedOutputs(self)

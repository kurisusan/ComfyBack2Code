
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for FilterZeroMasksAndCorrespondingImages
class FilterZeroMasksAndCorrespondingImagesInputs(InputSlots):
    masks: Slot[Image]
    def __init__(self, node: "Node"):
        self.masks = Slot[Image](node, "masks", 'MASK')

class FilterZeroMasksAndCorrespondingImagesOutputs(OutputSlots):
    non_zero_masks_out: Slot[Image]
    non_zero_mask_images_out: Slot[Image]
    zero_mask_images_out: Slot[Image]
    zero_mask_images_out_indexes: Slot[Any]
    def __init__(self, node: "Node"):
        self.non_zero_masks_out = Slot[Image](node, "non_zero_masks_out", 'MASK')
        self.non_zero_mask_images_out = Slot[Image](node, "non_zero_mask_images_out", 'IMAGE')
        self.zero_mask_images_out = Slot[Image](node, "zero_mask_images_out", 'IMAGE')
        self.zero_mask_images_out_indexes = Slot[Any](node, "zero_mask_images_out_indexes", 'INDEXES')

class FilterZeroMasksAndCorrespondingImages(Node[FilterZeroMasksAndCorrespondingImagesInputs, FilterZeroMasksAndCorrespondingImagesOutputs]):
    """
    Original name: FilterZeroMasksAndCorrespondingImages
    Category: KJNodes/masking
    
Filter out all the empty (i.e. all zero) mask in masks  
Also filter out all the corresponding images in original_images by indexes if provide  
  
original_images (optional): If provided, need have same length as masks.


    Inputs:
        - masks (Image)

    Outputs:
        - non_zero_masks_out (Image)
        - non_zero_mask_images_out (Image)
        - zero_mask_images_out (Image)
        - zero_mask_images_out_indexes (Any)
    """
    _original_name: str = 'FilterZeroMasksAndCorrespondingImages'

    def __init__(self, masks: Slot[Image]):
        super().__init__(**{"masks": masks})
        self.inputs = FilterZeroMasksAndCorrespondingImagesInputs(self)
        self.outputs = FilterZeroMasksAndCorrespondingImagesOutputs(self)

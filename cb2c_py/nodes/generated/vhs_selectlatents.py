
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for VHS_SelectLatents
class VHS_SelectLatentsInputs(InputSlots):
    latent: Slot[Latent]
    indexes: Slot[str]
    err_if_missing: Slot[bool]
    err_if_empty: Slot[bool]
    def __init__(self, node: "Node"):
        self.latent = Slot[Latent](node, "latent", 'LATENT')
        self.indexes = Slot[str](node, "indexes", 'STRING')
        self.err_if_missing = Slot[bool](node, "err_if_missing", 'BOOLEAN')
        self.err_if_empty = Slot[bool](node, "err_if_empty", 'BOOLEAN')

class VHS_SelectLatentsOutputs(OutputSlots):
    latent: Slot[Latent]
    def __init__(self, node: "Node"):
        self.latent = Slot[Latent](node, "LATENT", 'LATENT')

class VHS_SelectLatents(Node[VHS_SelectLatentsInputs, VHS_SelectLatentsOutputs]):
    """
    Original name: VHS_SelectLatents
    Category: Video Helper Suite 🎥🅥🅗🅢/latent
    Use comma-separated indexes to select items in the given order.
Supports negative indexes, python-style ranges (end index excluded),
as well as range step.

Acceptable entries (assuming 16 items provided, so idxs 0 to 15 exist):
0         -> Returns [0]
-1        -> Returns [15]
0, 1, 13  -> Returns [0, 1, 13]
0:5, 13   -> Returns [0, 1, 2, 3, 4, 13]
0:-1      -> Returns [0, 1, 2, ..., 13, 14]
0:5:-1    -> Returns [4, 3, 2, 1, 0]
0:5:2     -> Returns [0, 2, 4]
::-1     -> Returns [15, 14, 13, ..., 2, 1, 0]


    Inputs:
        - latent (Latent)
        - indexes (str) (default: '0')
        - err_if_missing (bool) (default: True)
        - err_if_empty (bool) (default: True)

    Outputs:
        - latent (Latent)
    """
    _original_name: str = 'VHS_SelectLatents'

    def __init__(self, latent: Slot[Latent], indexes: str = '0', err_if_missing: bool = True, err_if_empty: bool = True):
        super().__init__(**{"latent": latent, "indexes": indexes, "err_if_missing": err_if_missing, "err_if_empty": err_if_empty})
        self.inputs = VHS_SelectLatentsInputs(self)
        self.outputs = VHS_SelectLatentsOutputs(self)


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for VHS_SplitLatents
class VHS_SplitLatentsInputs(InputSlots):
    latents: Slot[Latent]
    split_index: Slot[int]
    def __init__(self, node: "Node"):
        self.latents = Slot[Latent](node, "latents", 'LATENT')
        self.split_index = Slot[int](node, "split_index", 'INT')

class VHS_SplitLatentsOutputs(OutputSlots):
    latent_a: Slot[Latent]
    a_count: Slot[int]
    latent_b: Slot[Latent]
    b_count: Slot[int]
    def __init__(self, node: "Node"):
        self.latent_a = Slot[Latent](node, "LATENT_A", 'LATENT')
        self.a_count = Slot[int](node, "A_count", 'INT')
        self.latent_b = Slot[Latent](node, "LATENT_B", 'LATENT')
        self.b_count = Slot[int](node, "B_count", 'INT')

class VHS_SplitLatents(Node[VHS_SplitLatentsInputs, VHS_SplitLatentsOutputs]):
    """
    Original name: VHS_SplitLatents
    Category: Video Helper Suite 🎥🅥🅗🅢/latent
    Split Latents 🎥🅥🅗🅢<div style="font-size: 0.8em"><div id=VHS_shortdesc>Split a set of latents into two groups</div></div><div style="font-size: 0.8em"><div vhs_title="Inputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Inputs: <div vhs_title="latents" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">latents: The latents to be split.</div></div></div></div><div vhs_title="Outputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Outputs: <div vhs_title="LATENT_A" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">LATENT_A: The first group of latents</div></div><div vhs_title="A_count" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">A_count: The number of latents in group A. This will be equal to split_index unless the latents input has length less than split_index</div></div><div vhs_title="LATENT_B" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">LATENT_B: The second group of latents</div></div><div vhs_title="B_count" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">B_count: The number of latents in group B</div></div></div></div><div vhs_title="Widgets" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Widgets: <div vhs_title="split_index" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">split_index: The index of the first latent that will be in the second output groups.</div></div></div></div></div>

    Inputs:
        - latents (Latent)
        - split_index (int) (default: 0)

    Outputs:
        - latent_a (Latent)
        - a_count (int)
        - latent_b (Latent)
        - b_count (int)
    """
    _original_name: str = 'VHS_SplitLatents'

    def __init__(self, latents: Slot[Latent], split_index: int = 0):
        super().__init__(**{"latents": latents, "split_index": split_index})
        self.inputs = VHS_SplitLatentsInputs(self)
        self.outputs = VHS_SplitLatentsOutputs(self)

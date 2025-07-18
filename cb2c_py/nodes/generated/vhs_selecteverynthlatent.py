
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for VHS_SelectEveryNthLatent
class VHS_SelectEveryNthLatentInputs(InputSlots):
    latents: Slot[Latent]
    select_every_nth: Slot[int]
    skip_first_latents: Slot[int]
    def __init__(self, node: "Node"):
        self.latents = Slot[Latent](node, "latents", 'LATENT')
        self.select_every_nth = Slot[int](node, "select_every_nth", 'INT')
        self.skip_first_latents = Slot[int](node, "skip_first_latents", 'INT')

class VHS_SelectEveryNthLatentOutputs(OutputSlots):
    latent: Slot[Latent]
    count: Slot[int]
    def __init__(self, node: "Node"):
        self.latent = Slot[Latent](node, "LATENT", 'LATENT')
        self.count = Slot[int](node, "count", 'INT')

class VHS_SelectEveryNthLatent(Node[VHS_SelectEveryNthLatentInputs, VHS_SelectEveryNthLatentOutputs]):
    """
    Original name: VHS_SelectEveryNthLatent
    Category: Video Helper Suite 🎥🅥🅗🅢/latent
    Select Every Nth Latent 🎥🅥🅗🅢<div style="font-size: 0.8em"><div id=VHS_shortdesc>Keep only 1 latent for every interval</div></div><div style="font-size: 0.8em"><div vhs_title="Inputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Inputs: <div vhs_title="latents" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">latents: The input latent</div></div></div></div><div vhs_title="Outputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Outputs: <div vhs_title="LATENT" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">LATENT: The output latents</div></div><div vhs_title="count" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">count: The number of latents in the input</div></div></div></div><div vhs_title="Widgets" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Widgets: <div vhs_title="select_every_nth" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">select_every_nth: The interval from which one frame is kept. 1 means no frames are skipped.</div></div><div vhs_title="skip_first_latents" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">skip_first_latents: A number of frames which that is skipped from the start. This applies before select_every_nth. As a result, multiple copies of the node can each have a different skip_first_frames to divide the latent into groups</div></div></div></div></div>

    Inputs:
        - latents (Latent)
        - select_every_nth (int) (default: 1)
        - skip_first_latents (int) (default: 0)

    Outputs:
        - latent (Latent)
        - count (int)
    """
    _original_name: str = 'VHS_SelectEveryNthLatent'

    def __init__(self, latents: Slot[Latent], select_every_nth: int = 1, skip_first_latents: int = 0):
        super().__init__(**{"latents": latents, "select_every_nth": select_every_nth, "skip_first_latents": skip_first_latents})
        self.inputs = VHS_SelectEveryNthLatentInputs(self)
        self.outputs = VHS_SelectEveryNthLatentOutputs(self)

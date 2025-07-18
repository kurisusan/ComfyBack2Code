
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for VHS_SelectFilename
class VHS_SelectFilenameInputs(InputSlots):
    filenames: Slot[Any]
    index: Slot[int]
    def __init__(self, node: "Node"):
        self.filenames = Slot[Any](node, "filenames", 'VHS_FILENAMES')
        self.index = Slot[int](node, "index", 'INT')

class VHS_SelectFilenameOutputs(OutputSlots):
    filename: Slot[str]
    def __init__(self, node: "Node"):
        self.filename = Slot[str](node, "Filename", 'STRING')

class VHS_SelectFilename(Node[VHS_SelectFilenameInputs, VHS_SelectFilenameOutputs]):
    """
    Original name: VHS_SelectFilename
    Category: Video Helper Suite 🎥🅥🅗🅢
    VAE Select Filename 🎥🅥🅗🅢<div style="font-size: 0.8em"><div id=VHS_shortdesc>Select a single filename from the VHS_FILENAMES output by a Video Combine and return it as a string</div></div><div style="font-size: 0.8em">Take care when combining this node with Prune Outputs. The VHS_FILENAMES object is immutable and will always contain the full list of output files, but execution order is undefined behavior (currently, Prune Outputs will generally execute first) and SelectFilename may return a path to a file that no longer exists.</div><div style="font-size: 0.8em"><div vhs_title="Inputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Inputs: <div vhs_title="filenames" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">filenames: A VHS_FILENAMES from a Video Combine node</div></div></div></div><div vhs_title="Outputs" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Outputs: <div vhs_title="filename" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">filename: A string representation of the full output path for the chosen file</div></div></div></div><div vhs_title="Widgets" style="display: flex; font-size: 0.8em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">Widgets: <div vhs_title="index" style="display: flex; font-size: 1em" class="VHS_collapse"><div style="color: #AAA; height: 1.5em;">[<span style="font-family: monospace">-</span>]</div><div style="width: 100%">index: The index of which file should be selected. The default, -1, chooses the most complete output</div></div></div></div></div>

    Inputs:
        - filenames (Any)
        - index (int) (default: -1)

    Outputs:
        - filename (str)
    """
    _original_name: str = 'VHS_SelectFilename'

    def __init__(self, filenames: Slot[Any], index: int = -1):
        super().__init__(**{"filenames": filenames, "index": index})
        self.inputs = VHS_SelectFilenameInputs(self)
        self.outputs = VHS_SelectFilenameOutputs(self)

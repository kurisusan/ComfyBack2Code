
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for ControlNetPreprocessorSelector
class ControlNetPreprocessorSelectorInputs(InputSlots):
    preprocessor: Slot[str]
    def __init__(self, node: "Node"):
        self.preprocessor = Slot[str](node, "preprocessor", ['none', 'BAE-NormalMapPreprocessor', 'OneFormer-COCO-SemSegPreprocessor', 'OneFormer-ADE20K-SemSegPreprocessor', 'TilePreprocessor', 'TTPlanet_TileGF_Preprocessor', 'TTPlanet_TileSimple_Preprocessor', 'SAMPreprocessor', 'AnyLineArtPreprocessor_aux', 'DepthAnythingV2Preprocessor', 'LineartStandardPreprocessor', 'ImageLuminanceDetector', 'ImageIntensityDetector', 'AnimeLineArtPreprocessor', 'DensePosePreprocessor', 'PiDiNetPreprocessor', 'DWPreprocessor', 'AnimalPosePreprocessor', 'ShufflePreprocessor', 'Zoe-DepthMapPreprocessor', 'ScribblePreprocessor', 'Scribble_XDoG_Preprocessor', 'Scribble_PiDiNet_Preprocessor', 'DepthAnythingPreprocessor', 'Zoe_DepthAnythingPreprocessor', 'DSINE-NormalMapPreprocessor', 'PyraCannyPreprocessor', 'Manga2Anime_LineArt_Preprocessor', 'MeshGraphormer-DepthMapPreprocessor', 'Metric3D-DepthMapPreprocessor', 'Metric3D-NormalMapPreprocessor', 'UniFormer-SemSegPreprocessor', 'SemSegPreprocessor', 'CannyEdgePreprocessor', 'ColorPreprocessor', 'BinaryPreprocessor', 'M-LSDPreprocessor', 'MiDaS-NormalMapPreprocessor', 'MiDaS-DepthMapPreprocessor', 'AnimeFace_SemSegPreprocessor', 'LeReS-DepthMapPreprocessor', 'TEEDPreprocessor', 'OpenposePreprocessor', 'HEDPreprocessor', 'FakeScribblePreprocessor', 'MediaPipe-FaceMeshPreprocessor', 'LineArtPreprocessor'])

class ControlNetPreprocessorSelectorOutputs(OutputSlots):
    preprocessor: Slot[str]
    def __init__(self, node: "Node"):
        self.preprocessor = Slot[str](node, "preprocessor", ['none', 'BAE-NormalMapPreprocessor', 'OneFormer-COCO-SemSegPreprocessor', 'OneFormer-ADE20K-SemSegPreprocessor', 'TilePreprocessor', 'TTPlanet_TileGF_Preprocessor', 'TTPlanet_TileSimple_Preprocessor', 'SAMPreprocessor', 'AnyLineArtPreprocessor_aux', 'DepthAnythingV2Preprocessor', 'LineartStandardPreprocessor', 'ImageLuminanceDetector', 'ImageIntensityDetector', 'AnimeLineArtPreprocessor', 'DensePosePreprocessor', 'PiDiNetPreprocessor', 'DWPreprocessor', 'AnimalPosePreprocessor', 'ShufflePreprocessor', 'Zoe-DepthMapPreprocessor', 'ScribblePreprocessor', 'Scribble_XDoG_Preprocessor', 'Scribble_PiDiNet_Preprocessor', 'DepthAnythingPreprocessor', 'Zoe_DepthAnythingPreprocessor', 'DSINE-NormalMapPreprocessor', 'PyraCannyPreprocessor', 'Manga2Anime_LineArt_Preprocessor', 'MeshGraphormer-DepthMapPreprocessor', 'Metric3D-DepthMapPreprocessor', 'Metric3D-NormalMapPreprocessor', 'UniFormer-SemSegPreprocessor', 'SemSegPreprocessor', 'CannyEdgePreprocessor', 'ColorPreprocessor', 'BinaryPreprocessor', 'M-LSDPreprocessor', 'MiDaS-NormalMapPreprocessor', 'MiDaS-DepthMapPreprocessor', 'AnimeFace_SemSegPreprocessor', 'LeReS-DepthMapPreprocessor', 'TEEDPreprocessor', 'OpenposePreprocessor', 'HEDPreprocessor', 'FakeScribblePreprocessor', 'MediaPipe-FaceMeshPreprocessor', 'LineArtPreprocessor'])

class ControlNetPreprocessorSelector(Node[ControlNetPreprocessorSelectorInputs, ControlNetPreprocessorSelectorOutputs]):
    """
    Original name: ControlNetPreprocessorSelector
    Category: ControlNet Preprocessors
    

    Inputs:
        - preprocessor (str)

    Outputs:
        - preprocessor (str)
    """
    _original_name: str = 'ControlNetPreprocessorSelector'

    def __init__(self, preprocessor: str):
        super().__init__(**{"preprocessor": preprocessor})
        self.inputs = ControlNetPreprocessorSelectorInputs(self)
        self.outputs = ControlNetPreprocessorSelectorOutputs(self)

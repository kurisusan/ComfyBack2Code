
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for CreateGradientFromCoords
class CreateGradientFromCoordsInputs(InputSlots):
    coordinates: Slot[str]
    frame_width: Slot[int]
    frame_height: Slot[int]
    start_color: Slot[str]
    end_color: Slot[str]
    multiplier: Slot[float]
    def __init__(self, node: "Node"):
        self.coordinates = Slot[str](node, "coordinates", 'STRING')
        self.frame_width = Slot[int](node, "frame_width", 'INT')
        self.frame_height = Slot[int](node, "frame_height", 'INT')
        self.start_color = Slot[str](node, "start_color", 'STRING')
        self.end_color = Slot[str](node, "end_color", 'STRING')
        self.multiplier = Slot[float](node, "multiplier", 'FLOAT')

class CreateGradientFromCoordsOutputs(OutputSlots):
    image: Slot[Image]
    def __init__(self, node: "Node"):
        self.image = Slot[Image](node, "image", 'IMAGE')

class CreateGradientFromCoords(Node[CreateGradientFromCoordsInputs, CreateGradientFromCoordsOutputs]):
    """
    Original name: CreateGradientFromCoords
    Category: KJNodes/image
    
Creates a gradient image from coordinates.    


    Inputs:
        - coordinates (str)
        - frame_width (int) (default: 512)
        - frame_height (int) (default: 512)
        - start_color (str) (default: 'white')
        - end_color (str) (default: 'black')
        - multiplier (float) (default: 1.0)

    Outputs:
        - image (Image)
    """
    _original_name: str = 'CreateGradientFromCoords'

    def __init__(self, coordinates: str, frame_width: int = 512, frame_height: int = 512, start_color: str = 'white', end_color: str = 'black', multiplier: float = 1.0):
        super().__init__(**{"coordinates": coordinates, "frame_width": frame_width, "frame_height": frame_height, "start_color": start_color, "end_color": end_color, "multiplier": multiplier})
        self.inputs = CreateGradientFromCoordsInputs(self)
        self.outputs = CreateGradientFromCoordsOutputs(self)

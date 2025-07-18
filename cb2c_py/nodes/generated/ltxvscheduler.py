
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for LTXVScheduler
class LTXVSchedulerInputs(InputSlots):
    steps: Slot[int]
    max_shift: Slot[float]
    base_shift: Slot[float]
    stretch: Slot[bool]
    terminal: Slot[float]
    def __init__(self, node: "Node"):
        self.steps = Slot[int](node, "steps", 'INT')
        self.max_shift = Slot[float](node, "max_shift", 'FLOAT')
        self.base_shift = Slot[float](node, "base_shift", 'FLOAT')
        self.stretch = Slot[bool](node, "stretch", 'BOOLEAN')
        self.terminal = Slot[float](node, "terminal", 'FLOAT')

class LTXVSchedulerOutputs(OutputSlots):
    sigmas: Slot[Any]
    def __init__(self, node: "Node"):
        self.sigmas = Slot[Any](node, "SIGMAS", 'SIGMAS')

class LTXVScheduler(Node[LTXVSchedulerInputs, LTXVSchedulerOutputs]):
    """
    Original name: LTXVScheduler
    Category: sampling/custom_sampling/schedulers
    

    Inputs:
        - steps (int) (default: 20)
        - max_shift (float) (default: 2.05)
        - base_shift (float) (default: 0.95)
        - stretch (bool) (default: True)
          Stretch the sigmas to be in the range [terminal, 1].
        - terminal (float) (default: 0.1)
          The terminal value of the sigmas after stretching.

    Outputs:
        - sigmas (Any)
    """
    _original_name: str = 'LTXVScheduler'

    def __init__(self, steps: int = 20, max_shift: float = 2.05, base_shift: float = 0.95, stretch: bool = True, terminal: float = 0.1):
        super().__init__(**{"steps": steps, "max_shift": max_shift, "base_shift": base_shift, "stretch": stretch, "terminal": terminal})
        self.inputs = LTXVSchedulerInputs(self)
        self.outputs = LTXVSchedulerOutputs(self)

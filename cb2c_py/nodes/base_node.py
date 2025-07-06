# comfyui/back2code/nodes/base_node.py

class Slot:
    """Represents a single input or output slot on a node."""
    def __init__(self, node, slot_name):
        self.node = node
        self.name = slot_name

class InputSlots:
    """A container for the input slots of a node."""
    def __init__(self, node, input_info):
        self._node = node
        self._slot_names = list(input_info.keys())
        for name in self._slot_names:
            setattr(self, name, Slot(node, name))

    def __getitem__(self, key):
        return getattr(self, key)

class OutputSlots:
    """A container for the output slots of a node."""
    def __init__(self, node, output_info):
        self._node = node
        self._slot_names = output_info
        for name in self._slot_names:
            setattr(self, name, Slot(node, name))

    def __getitem__(self, key):
        return getattr(self, key)


class Node:
    """
    The base class for all ComfyUI nodes in the ComfyBack2Code framework.
    It stores the instance-specific input values and provides access to input/output slots.
    """
    def __init__(self, **kwargs):
        self.original_name = self._original_name
        self.input_values = kwargs
        
        # These will be populated by the generated subclasses
        self.inputs = InputSlots(self, self.get_inputs())
        self.outputs = OutputSlots(self, self.get_outputs())
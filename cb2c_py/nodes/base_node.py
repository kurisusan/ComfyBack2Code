# comfyui/back2Code/nodes/base_node.py

from typing import Optional, TypeVar, Generic, List


# Define common ComfyUI data types for type hinting.
# These are placeholder classes used for static analysis.
class Model: ...
class Conditioning: ...
class Latent: ...
class Image: ...
class Vae: ...
class Clip: ...

# A generic type for the slot's data
T = TypeVar("T")


class Slot(Generic[T]):
    """Represents a single input or output slot on a node."""

    def __init__(self, node: "Node", name: str, slot_type: any):
        self._node = node
        self._name = name
        self._type = slot_type

    def __str__(self):
        return f"Slot(node={self._node}, name='{self._name}', type='{self._type}')"


class InputSlots:
    """Base class for a node's input slots."""
    pass


class OutputSlots:
    """Base class for a node's output slots."""
    pass


I = TypeVar("I", bound=InputSlots)
O = TypeVar("O", bound=OutputSlots)


class Node(Generic[I, O]):
    """
    The base class for all ComfyUI nodes in the ComfyBack2Code framework.
    It stores the instance-specific input values and provides access to input/output slots.
    """

    _original_name: str = "BaseNode"
    inputs: I
    outputs: O

    def __init__(self, **kwargs):
        self.original_name = self._original_name
        self.input_values = kwargs
        self.id: Optional[int] = None
        self.workflow: Optional["Workflow"] = None

    def get_outputs(self) -> List[str]:
        """
        Returns a list of the node's output slot names.
        """
        return [slot._name for slot in vars(self.outputs).values()]

    def to_dict(self):
        """Serializes the node to a dictionary for the workflow."""
        return {
            "inputs": self.input_values,
            "class_type": self.original_name,
        }

# comfyui/back2Code/nodes/base_node.py

from typing import Optional, TypeVar, Generic, List, Dict, Any


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
    It also allows for arbitrary properties to be set on the node instance.
    """

    _original_name: str = "BaseNode"
    inputs: I
    outputs: O
    _properties: Dict[str, Any]

    def __init__(self, **kwargs):
        self.original_name = self._original_name
        self.input_values = kwargs
        self.id: Optional[int] = None
        self.workflow: Optional["Workflow"] = None
        # Use super().__setattr__ to avoid our override
        super().__setattr__("_properties", {})

    def __setattr__(self, name: str, value: Any):
        # Known attributes are set directly to avoid recursion.
        # We also avoid intercepting private attributes.
        known_attrs = ('original_name', 'input_values', 'id', 'workflow', 'inputs', 'outputs')
        if name.startswith('_') or name in known_attrs:
            super().__setattr__(name, value)
        else:
            # Store other attributes in the _properties dictionary.
            self._properties[name] = value

    def __getattr__(self, name: str) -> Any:
        # This is called as a fallback when an attribute is not found.
        # We check our _properties dict to provide dynamic attributes.
        if '_properties' in self.__dict__ and name in self._properties:
            return self._properties[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def get_outputs(self) -> List[str]:
        """
        Returns a list of the node's output slot names.
        """
        return [slot._name for slot in vars(self.outputs).values()]

    def to_dict(self):
        """Serializes the node to a dictionary for the workflow."""
        # Merge the constructor inputs and the dynamic properties
        node_dict = {
            "inputs": {**self.input_values, **self._properties},
            "class_type": self.original_name,
        }
        return node_dict

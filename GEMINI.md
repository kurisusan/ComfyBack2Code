# ComfyBack2Code Project Context

## 1. Core Objective

The primary goal of the `ComfyBack2Code` project is to enable developers to create, manage, and execute ComfyUI workflows programmatically using Python. This provides a scriptable, version-controllable, and automatable alternative to the graphical user interface.

## 2. Key Architectural Components

*   **Workflow Builder (`lib/workflow.py`):** A Python class-based interface for constructing a workflow graph. It allows users to add nodes and define connections between them.
*   **Node Definitions (`nodes/`):** Represents the available ComfyUI nodes. The strategy is to dynamically generate these node definitions by querying a running ComfyUI instance's API (`/object_info` endpoint). This avoids manual maintenance and automatically supports custom nodes.
*   **Workflow Runner (`runner-example.py`):** A component responsible for taking a generated workflow JSON and executing it via the ComfyUI API (`/prompt` endpoint).
*   **Dependency Management:** The project uses `custom-nodes.txt` to manage custom node dependencies for ComfyUI.

## 3. Development Plan

1.  **Implement Node Discovery:** Create a service to fetch node definitions from the ComfyUI API and cache them locally.
2.  **Dynamic Node Factory:** Build a mechanism to dynamically create Python classes based on the discovered node definitions. This will allow for intuitive, code-completion-friendly workflow scripting.
3.  **Refine Workflow Builder:** Integrate the dynamic nodes into the `Workflow` class, including methods for connecting node outputs to inputs.
4.  **Implement API Runner:** Develop the functionality to submit the built workflow to the ComfyUI API and retrieve the results.
5.  **Create Examples:** Build clear examples demonstrating how to define and run a complete workflow from end to end.

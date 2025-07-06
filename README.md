# ComfyBack2Code

**ComfyBack2Code** is a framework for developers to build, manage, and execute ComfyUI workflows programmatically using Python. It provides a scriptable, version-controllable, and automatable alternative to the graphical user interface.

The goal is to make **ComfyUI workflow creation 100% scriptable** in Python, from node definition to final execution.

---

## 🎯 Core Objective

The primary goal of the `ComfyBack2Code` project is to enable developers to create, manage, and execute ComfyUI workflows programmatically using Python. This provides a scriptable, version-controllable, and automatable alternative to the graphical user interface.

---

## 🧱 Key Components

The project is built around a few key components:

- **Workflow Builder (`lib/workflow.py`):** A Python class-based interface for constructing a workflow graph. It allows users to add nodes and define connections between them.
- **Dynamic Node Generation (`nodes/`):** Instead of manually defining each node, this project dynamically generates Python classes for all available ComfyUI nodes (including custom nodes) by querying the API (`/object_info` endpoint) of a running ComfyUI instance.
  - `nodes/node_discovery.py`: Fetches the node definitions.
  - `nodes/generate_nodes.py`: Creates the corresponding Python modules in `nodes/generated/`.
- **Workflow Runner (`example/runner/simple.py`):** An example component responsible for taking a generated workflow JSON and executing it via the ComfyUI API (`/prompt` endpoint).
- **Dependency Management (`custom-nodes.txt`):** A simple text file to manage custom node dependencies for your ComfyUI setup.

---

## 🚀 Getting Started

Here's how to get started with creating and running a workflow in code:

### 1. Set up ComfyUI

You need a running ComfyUI instance with the API enabled. You can use the provided Docker setup for a quick start:

```bash
docker compose -f docker/docker-compose.yml up -d
```

This will start a ComfyUI instance with the necessary configurations.

### 2. Install Custom Nodes

Add the git repository URLs of any custom nodes you need to `custom-nodes.txt`. The `docker/custom-nodes-loader.sh` script will automatically clone them into the correct directory when the container starts.

### 3. Generate Python Node Classes

Once your ComfyUI instance is running (with all custom nodes loaded), generate the Python wrapper classes:

```bash
# Make sure your environment is set up to connect to the ComfyUI API
# (e.g., by setting API_URL in your environment or .env file)
python -m cb2c_py/nodes/generate_nodes.py
```

This will populate the `nodes/generated/` directory with Python modules corresponding to each ComfyUI node.

### 4. Build a Workflow

Create a Python script to define your workflow using the `Workflow` class and the generated node classes. See `example/workflow/simple.py` for a template.

```python
# example/workflow/simple.py
from lib.workflow import Workflow
from nodes.generated import KSampler, CheckpointLoaderSimple, EmptyLatentImage, VAEDecode, SaveImage

def create_simple_workflow():
    wf = Workflow()

    # 1. Load Checkpoint
    chkpt_loader = CheckpointLoaderSimple(ckpt_name="v1-5-pruned-emaonly.safetensors")

    # 2. Create a latent image
    latent_image = EmptyLatentImage(width=512, height=512, batch_size=1)

    # 3. KSampler
    sampler = KSampler(
        seed=42,
        steps=20,
        cfg=8.0,
        sampler_name="euler",
        scheduler="normal",
        model=chkpt_loader.outputs["MODEL"],
        positive=chkpt_loader.outputs["CLIP"].encode("a beautiful photograph"),
        negative=chkpt_loader.outputs["CLIP"].encode("ugly, deformed"),
        latent_image=latent_image.outputs["LATENT"]
    )

    # 4. Decode the latent image
    vae_decode = VAEDecode(
        samples=sampler.outputs["LATENT"],
        vae=chkpt_loader.outputs["VAE"]
    )

    # 5. Save the final image
    SaveImage(images=vae_decode.outputs["IMAGE"])

    return wf.to_prompt()

if __name__ == "__main__":
    import json
    workflow_json = create_simple_workflow()
    print(json.dumps(workflow_json, indent=2))
```

### 5. Run the Workflow

Use the `example/runner/simple.py` script to execute the workflow against the ComfyUI API.

```bash
python -m example/runner/simple.py
```

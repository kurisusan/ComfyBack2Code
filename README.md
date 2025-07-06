# ComfyBack2Code

**ComfyBack2Code** is a hybrid framework for developers and creators to build, run, and iterate on generation workflows via ComfyUI — without relying on the graphical interface.

The goal is to make **ComfyUI workflow creation 100% scriptable**, modular, version-controlled, and automatable.

---

## 🎯 Project Goals

- Write ComfyUI workflows **in Python or a custom lightweight DSL**
- Support **loops, conditions, functions, dynamic prompt generation**
- **Automatically generate** ComfyUI-compatible JSON workflows
- Run workflows **via the ComfyUI API**, either locally or inside Docker
- Simplify **custom node** and **model** management with dependency files
- Provide a modern, clean, and powerful **developer experience (DX)**

---

## 🧱 Architecture

The project is split into 2 layers:

### 1. `Builder` – Workflow Construction

- Python interface to build a ComfyUI node graph
- Outputs valid JSON compatible with ComfyUI
- Example:
  TODO

### 2. `Runner` – Workflow Execution

- Uses ComfyUI REST API to run the workflow
- Works locally or via encapsulated Docker container
- Can:
  - Launch inference
  - Fetch images / logs
  - Manage assets (prompts, models, outputs...)

---

## 📦 Dependency Management

- `models.txt` to declare models:
  ```txt
  sdxl|https://huggingface.co/stabilityai/sdxl-base-1.0/resolve/main/sdxl.safetensors
  ```
- `nodes.txt` to declare custom nodes:
  ```txt
  comfy_anime_colorizer|https://github.com/yourname/comfy-anime-colorizer
  ```

---

## 🚀 Example CLI Commands

```bash
# Compile a Python script into ComfyUI workflow JSON
comfyback2code compile workflows/my_script.py

# Run a workflow via ComfyUI API
comfyback2code run workflows/dragons.json

# Add a model or a custom node
comfyback2code install-model sdxl
comfyback2code install-node comfy_anime_colorizer
```

---

## 📚 Roadmap

- [x] Create a `WorkflowBuilder` in Python
- [x] Generate ComfyUI-compatible JSON
- [ ] Dockerize ComfyUI with API access
- [ ] Add API-based execution flow
- [ ] Add batch processing / CSV prompt input
- [ ] Support alternative DSL syntax
- [ ] Optional React or TUI frontend

---

## ❤️ Vision

ComfyBack2Code empowers **technical creators** to combine ComfyUI's visual modularity with the automation, readability, and scalability of code.

**Build workflows. Run them anywhere. Automate the impossible.**

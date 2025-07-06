#!/usr/bin/env python3

# comfyui/back2code/workflow-example.py

"""
This script demonstrates how to build a simple text-to-image workflow
programmatically using the ComfyBack2Code framework.
"""

from comfyui.back2code.lib.workflow import Workflow
from comfyui.back2code.nodes.generated import (
    CheckpointLoaderSimple,
    CLIPTextEncode,
    KSampler,
    EmptyLatentImage,
    VAEDecode,
    SaveImage,
)

def build_simple_workflow():
    """
    Creates a standard text-to-image workflow object.
    """
    wf = Workflow()

    # 1. Load the model checkpoint
    # Note: The class name is sanitized, but the `ckpt_name` is the actual model file.
    chkpt_loader = wf.add_node(CheckpointLoaderSimple(
        ckpt_name="v1-5-pruned-emaonly.safetensors"
    ))

    # 2. Create an empty latent image
    empty_latent = wf.add_node(EmptyLatentImage(
        width=512,
        height=512,
        batch_size=1
    ))

    # 3. Encode the positive prompt
    positive_prompt = wf.add_node(CLIPTextEncode(
        text="a beautiful photograph of a running horse",
        clip=None,
    ))

    # 4. Encode the negative prompt
    negative_prompt = wf.add_node(CLIPTextEncode(
        text="blurry, bad, low quality",
        clip=None,
    ))

    # 5. The KSampler node, which generates the image from the noise
    sampler = wf.add_node(KSampler(
        seed=12345,
        steps=20,
        cfg=8.0,
        sampler_name="euler",
        scheduler="normal",
        denoise=1.0,
        model=None,
        positive=None,
        negative=None,
        latent_image=None,
    ))

    # 6. Decode the latent image back into pixels
    vae_decode = wf.add_node(VAEDecode(
        samples=None,
        vae=None,
    ))

    # 7. Save the final image
    save_image = wf.add_node(SaveImage(
        filename_prefix="ComfyBack2Code_example",
        images=None,
    ))

    # 8. Connect the nodes together using the new, intuitive syntax
    print("Connecting workflow nodes...")
    wf.connect(chkpt_loader.outputs.MODEL, sampler.inputs.model)
    wf.connect(chkpt_loader.outputs.CLIP, positive_prompt.inputs.clip)
    wf.connect(chkpt_loader.outputs.CLIP, negative_prompt.inputs.clip)
    wf.connect(chkpt_loader.outputs.VAE, vae_decode.inputs.vae)
    wf.connect(empty_latent.outputs.LATENT, sampler.inputs.latent_image)
    wf.connect(positive_prompt.outputs.CONDITIONING, sampler.inputs.positive)
    wf.connect(negative_prompt.outputs.CONDITIONING, sampler.inputs.negative)
    wf.connect(sampler.outputs.LATENT, vae_decode.inputs.samples)
    wf.connect(vae_decode.outputs.IMAGE, save_image.inputs.images)

    return wf

if __name__ == "__main__":
    print("Building a simple text-to-image workflow...")
    workflow = build_simple_workflow()

    # The runner script will now handle the execution of the workflow.
    print("\nWorkflow built successfully.")
    print("You can now run the `runner-example.py` to execute this workflow.")

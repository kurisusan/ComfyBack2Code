#!/usr/bin/env python3

# comfyui/back2code/workflow-example.py

"""
This script demonstrates how to build a simple text-to-image workflow
programmatically using the ComfyBack2Code framework.
"""

from cb2c_py.lib.workflow import Workflow
from cb2c_py.nodes.generated import (
    CheckpointLoaderSimple,
    CLIPTextEncode,
    KSampler,
    EmptyLatentImage,
    VAEDecode,
    SaveImage,
)


def simple_image_workflow(
    pos_prompt: str,
    neg_prompt: str,
    seed: int,
    steps: int = 20,
):
    """
    Creates a standard text-to-image workflow object.
    """
    wf = Workflow()

    # 1. Load the model checkpoint
    chkpt_loader_node = CheckpointLoaderSimple(ckpt_name="v1-5-pruned-emaonly.safetensors")
    wf.add_node(chkpt_loader_node)

    # 2. Create an empty latent image
    empty_latent_node = EmptyLatentImage(width=512, height=512, batch_size=1)
    wf.add_node(empty_latent_node)

    # 3. Encode the positive prompt, connecting it to the checkpoint loader's CLIP output
    positive_prompt_node = CLIPTextEncode(
        text=pos_prompt,
        clip=chkpt_loader_node.outputs.clip,
    )
    wf.add_node(positive_prompt_node)

    # 4. Encode the negative prompt, also connecting it to the checkpoint loader's CLIP output
    negative_prompt_node = CLIPTextEncode(
            text=neg_prompt,
            clip=chkpt_loader_node.outputs.clip,
        )
    wf.add_node(negative_prompt_node)

    # 5. The KSampler node, which takes outputs from all previous nodes
    sampler_node = KSampler(
            seed=seed,
            steps=steps,
            cfg=8.0,
            sampler_name="euler",
            scheduler="normal",
            denoise=1.0,
            model=chkpt_loader_node.outputs.model,
            positive=positive_prompt_node.outputs.conditioning,
            negative=negative_prompt_node.outputs.conditioning,
            latent_image=empty_latent_node.outputs.latent,
        )
    wf.add_node(sampler_node)

    # 6. Decode the latent image back into pixels
    vae_decode_node = VAEDecode(
        samples=sampler_node.outputs.latent,
        vae=chkpt_loader_node.outputs.vae,
        )
    wf.add_node(vae_decode_node)

    # 7. Save the final image
    save_image_node = SaveImage(
            filename_prefix="ComfyBack2Code_example",
            images=vae_decode_node.outputs.image,
        )
    wf.add_node(save_image_node)

    # The connections are now defined directly when creating the nodes.
    # The wf.connect calls are no longer needed.

    return wf

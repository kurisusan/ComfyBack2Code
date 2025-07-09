from cb2c_py.lib.workflow import Workflow
from cb2c_py.nodes.generated import CLIPTextEncode
from cb2c_py.nodes.generated import ConditioningZeroOut
from cb2c_py.nodes.generated import DualCLIPLoader
from cb2c_py.nodes.generated import EmptySD3LatentImage
from cb2c_py.nodes.generated import FluxGuidance
from cb2c_py.nodes.generated import FluxKontextImageScale
from cb2c_py.nodes.generated import ImageStitch
from cb2c_py.nodes.generated import KSampler
from cb2c_py.nodes.generated import LoadImageOutput
from cb2c_py.nodes.generated import NunchakuFluxDiTLoader
from cb2c_py.nodes.generated import NunchakuWheelInstaller
from cb2c_py.nodes.generated import PreviewAny
from cb2c_py.nodes.generated import PreviewImage
from cb2c_py.nodes.generated import ReferenceLatent
from cb2c_py.nodes.generated import SaveImage
from cb2c_py.nodes.generated import VAEDecode
from cb2c_py.nodes.generated import VAEEncode
from cb2c_py.nodes.generated import VAELoader


def flux_kontext_dev_nunchaku():
    wf = Workflow()

    # Node: VAELoader (ID: 39)
    vaeloader_39 = VAELoader(vae_name="ae.safetensors")
    wf.add_node(vaeloader_39)

    # Note from MarkdownNote (ID: 190):
    # You can adjust the `cache_threshold` parameter to balance **image quality** and **inference speed**. A value of `0.12` typically offers a good trade-off.  Enable `cpu_offload` to **save GPU memory** if you're running into memory limits.

    # Note from MarkdownNote (ID: 178):
    # In addition to using **Image Stitch** to combine two images at a time, you can also encode individual images, then concatenate multiple latent conditions using the **ReferenceLatent** node, thus achieving the purpose of referencing multiple images. You can use the **EmptySD3LatentImage** node on the right to connect to **KSamper** and customize the size of the **latent_image**.

    # Note from MarkdownNote (ID: 175):
    # Use Ctrl + B to enable multipule image input.

    # Node: NunchakuWheelInstaller (ID: 191)
    nunchakuwheelinstaller_191 = NunchakuWheelInstaller(
        source="HuggingFace", version="v0.3.1"
    )
    wf.add_node(nunchakuwheelinstaller_191)

    # Note from MarkdownNote (ID: 184):
    # ## Tutorials [English](https://comfyui-wiki.com/en/tutorial/advanced/image/flux/flux-1-kontext) | [中文](https://comfyui-wiki.com/zh/tutorial/advanced/image/flux/flux-1-kontext) | [日本語](https://comfyui-wiki.com/ja/tutorial/advanced/image/flux/flux-1-kontext) | [한국어](https://comfyui-wiki.com/ko/tutorial/advanced/image/flux/flux-1-kontext) | [Français](https://comfyui-wiki.com/fr/tutorial/advanced/image/flux/flux-1-kontext) | [Español](https://comfyui-wiki.com/es/tutorial/advanced/image/flux/flux-1-kontext)  **Custom nodes**  [ComfyUI-nunchaku](https://github.com/mit-han-lab/ComfyUI-nunchaku)  **Diffusion model**  Download the model from [HuggingFace](https://huggingface.co/mit-han-lab/nunchaku-flux.1-kontext-dev) or [ModelScope](https://modelscope.cn/models/Lmxyy1999/nunchaku-flux.1-kontext-dev). - For **Blackwell (50-series) GPUs**:[svdq-fp4_r32-flux.1-kontext-dev.safetensors](https://huggingface.co/mit-han-lab/nunchaku-flux.1-kontext-dev/resolve/main/svdq-fp4_r32-flux.1-kontext-dev.safetensors) - **Other GPUs**：[svdq-int4_r32-flux.1-kontext-dev.safetensors](https://huggingface.co/mit-han-lab/nunchaku-flux.1-kontext-dev/resolve/main/svdq-int4_r32-flux.1-kontext-dev.safetensors)  **vae**  - [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/blob/main/split_files/vae/ae.safetensors)  **text encoder**  - [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors) - [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) or [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors)  Model Storage Location  ``` 📂 ComfyUI/ ├── 📂 models/ │   ├── 📂 diffusion_models/ │       ├── svdq-fp4_r32-flux.1-kontext-dev.safetensors # For Blackwell (50-series) GPUs │   │   └── svdq-int4_r32-flux.1-kontext-dev.safetensors │   ├── 📂 vae/ │   │   └── ae.safetensor │   └── 📂 text_encoders/ │       ├── clip_l.safetensors │       └── t5xxl_fp16.safetensors 或者 t5xxl_fp8_e4m3fn_scaled.safetensors ```

    # Note from MarkdownNote (ID: 193):
    # 1. Install [ComfyUI - nunchaku](https://github.com/mit-han-lab/ComfyUI-nunchaku) first. 2. Then, you need to install the Nunchaku Wheel to make sure the **Nunchaku FLUX DiT Loader** node can load normally. 3. Delete all other nodes in this workflow except the **Step - 0** group. 4. Use **Ctrl + B** to enable the **Step - 0** group. 5. Run the workflow. 6. After the Nunchaku wheel is installed successfully, restart ComfyUI and load this workflow from the template again.  If you have any trouble installing Nunchaku Wheel, please visit [ComfyUI - nunchaku](https://github.com/mit-han-lab/ComfyUI-nunchaku) for help.

    # Node: DualCLIPLoader (ID: 38)
    dualcliploader_38 = DualCLIPLoader(
        clip_name1="clip_l.safetensors",
        clip_name2="t5xxl_fp8_e4m3fn_scaled.safetensors",
        type="flux",
    )
    dualcliploader_38.device = "default"
    wf.add_node(dualcliploader_38)

    # Node: EmptySD3LatentImage (ID: 188)
    emptysd3latentimage_188 = EmptySD3LatentImage(width=1024, height=1024, batch_size=1)
    wf.add_node(emptysd3latentimage_188)

    # Node: NunchakuFluxDiTLoader (ID: 189)
    nunchakufluxditloader_189 = NunchakuFluxDiTLoader(
        model_path="svdq-fp4_r32-flux.1-kontext-dev.safetensors",
        cache_threshold=0,
        attention="nunchaku-fp16",
        cpu_offload="auto",
        device_id=0,
        data_type="bfloat16",
    )
    nunchakufluxditloader_189.i2f_mode = "enabled"
    wf.add_node(nunchakufluxditloader_189)

    # Node: LoadImageOutput (ID: 147)
    loadimageoutput_147 = LoadImageOutput(image="pasted/image.png [output]")
    loadimageoutput_147.upload = False
    wf.add_node(loadimageoutput_147)

    # Node: LoadImageOutput (ID: 142)
    loadimageoutput_142 = LoadImageOutput(
        image="signal-2025-02-09-092657.jpeg [output]"
    )
    loadimageoutput_142.upload = False
    wf.add_node(loadimageoutput_142)

    # Node: PreviewAny (ID: 192)
    previewany_192 = PreviewAny(source=nunchakuwheelinstaller_191.outputs.status)
    wf.add_node(previewany_192)

    # Node: CLIPTextEncode (ID: 6)
    cliptextencode_6 = CLIPTextEncode(
        clip=dualcliploader_38.outputs.clip, text="Swap the cat and the dog positions"
    )
    wf.add_node(cliptextencode_6)

    # Node: ImageStitch (ID: 146)
    imagestitch_146 = ImageStitch(
        image1=loadimageoutput_142.outputs.image,
        direction="right",
        match_image_size=True,
        spacing_width=0,
        spacing_color="white",
    )
    imagestitch_146.image2 = loadimageoutput_147.outputs.image
    wf.add_node(imagestitch_146)

    # Node: ConditioningZeroOut (ID: 135)
    conditioningzeroout_135 = ConditioningZeroOut(
        conditioning=cliptextencode_6.outputs.conditioning
    )
    wf.add_node(conditioningzeroout_135)

    # Node: FluxKontextImageScale (ID: 42)
    fluxkontextimagescale_42 = FluxKontextImageScale(
        image=imagestitch_146.outputs.image
    )
    wf.add_node(fluxkontextimagescale_42)

    # Node: VAEEncode (ID: 124)
    vaeencode_124 = VAEEncode(
        pixels=fluxkontextimagescale_42.outputs.image, vae=vaeloader_39.outputs.vae
    )
    wf.add_node(vaeencode_124)

    # Node: PreviewImage (ID: 173)
    previewimage_173 = PreviewImage(images=fluxkontextimagescale_42.outputs.image)
    wf.add_node(previewimage_173)

    # Node: ReferenceLatent (ID: 177)
    referencelatent_177 = ReferenceLatent(
        conditioning=cliptextencode_6.outputs.conditioning
    )
    referencelatent_177.latent = vaeencode_124.outputs.latent
    wf.add_node(referencelatent_177)

    # Node: FluxGuidance (ID: 35)
    fluxguidance_35 = FluxGuidance(
        conditioning=referencelatent_177.outputs.conditioning, guidance=2.5
    )
    wf.add_node(fluxguidance_35)

    # Node: KSampler (ID: 31)
    ksampler_31 = KSampler(
        model=nunchakufluxditloader_189.outputs.model,
        positive=fluxguidance_35.outputs.conditioning,
        negative=conditioningzeroout_135.outputs.conditioning,
        latent_image=vaeencode_124.outputs.latent,
        seed=33520218837729,
        steps=20,
        cfg=20,
        sampler_name="euler",
        scheduler="normal",
        denoise=0.5,
    )
    wf.add_node(ksampler_31)

    # Node: VAEDecode (ID: 8)
    vaedecode_8 = VAEDecode(
        samples=ksampler_31.outputs.latent, vae=vaeloader_39.outputs.vae
    )
    wf.add_node(vaedecode_8)

    # Node: SaveImage (ID: 136)
    saveimage_136 = SaveImage(
        images=vaedecode_8.outputs.image, filename_prefix="kontext/test/kxt_test_"
    )
    wf.add_node(saveimage_136)

    return wf


# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for KSamplerVariationsWithNoise_
class KSamplerVariationsWithNoise_Inputs(InputSlots):
    model: Slot[Model]
    latent_image: Slot[Latent]
    main_seed: Slot[Any]
    steps: Slot[int]
    cfg: Slot[float]
    sampler_name: Slot[str]
    scheduler: Slot[str]
    positive: Slot[Conditioning]
    negative: Slot[Conditioning]
    variation_strength: Slot[float]
    variation_seed: Slot[Any]
    denoise: Slot[float]
    def __init__(self, node: "Node"):
        self.model = Slot[Model](node, "model", 'MODEL')
        self.latent_image = Slot[Latent](node, "latent_image", 'LATENT')
        self.main_seed = Slot[Any](node, "main_seed", 'INT:seed')
        self.steps = Slot[int](node, "steps", 'INT')
        self.cfg = Slot[float](node, "cfg", 'FLOAT')
        self.sampler_name = Slot[str](node, "sampler_name", ['euler', 'euler_cfg_pp', 'euler_ancestral', 'euler_ancestral_cfg_pp', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_2s_ancestral_cfg_pp', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_cfg_pp', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ipndm', 'ipndm_v', 'deis', 'res_multistep', 'res_multistep_cfg_pp', 'res_multistep_ancestral', 'res_multistep_ancestral_cfg_pp', 'gradient_estimation', 'gradient_estimation_cfg_pp', 'er_sde', 'seeds_2', 'seeds_3', 'ddim', 'uni_pc', 'uni_pc_bh2'])
        self.scheduler = Slot[str](node, "scheduler", ['simple', 'sgm_uniform', 'karras', 'exponential', 'ddim_uniform', 'beta', 'normal', 'linear_quadratic', 'kl_optimal'])
        self.positive = Slot[Conditioning](node, "positive", 'CONDITIONING')
        self.negative = Slot[Conditioning](node, "negative", 'CONDITIONING')
        self.variation_strength = Slot[float](node, "variation_strength", 'FLOAT')
        self.variation_seed = Slot[Any](node, "variation_seed", 'INT:seed')
        self.denoise = Slot[float](node, "denoise", 'FLOAT')

class KSamplerVariationsWithNoise_Outputs(OutputSlots):
    latent: Slot[Latent]
    def __init__(self, node: "Node"):
        self.latent = Slot[Latent](node, "LATENT", 'LATENT')

class KSamplerVariationsWithNoise_(Node[KSamplerVariationsWithNoise_Inputs, KSamplerVariationsWithNoise_Outputs]):
    """
    Original name: KSamplerVariationsWithNoise+
    Category: essentials/sampling
    

    Inputs:
        - model (Model)
        - latent_image (Latent)
        - main_seed (Any) (default: 0)
        - steps (int) (default: 20)
        - cfg (float) (default: 8.0)
        - sampler_name (str)
        - scheduler (str)
        - positive (Conditioning)
        - negative (Conditioning)
        - variation_strength (float) (default: 0.17)
        - variation_seed (Any) (default: 12345)
        - denoise (float) (default: 1.0)

    Outputs:
        - latent (Latent)
    """
    _original_name: str = 'KSamplerVariationsWithNoise+'

    def __init__(self, model: Slot[Model], latent_image: Slot[Latent], sampler_name: str, scheduler: str, positive: Slot[Conditioning], negative: Slot[Conditioning], main_seed: Slot[Any] = 0, steps: int = 20, cfg: float = 8.0, variation_strength: float = 0.17, variation_seed: Slot[Any] = 12345, denoise: float = 1.0):
        super().__init__(**{"model": model, "latent_image": latent_image, "main_seed": main_seed, "steps": steps, "cfg": cfg, "sampler_name": sampler_name, "scheduler": scheduler, "positive": positive, "negative": negative, "variation_strength": variation_strength, "variation_seed": variation_seed, "denoise": denoise})
        self.inputs = KSamplerVariationsWithNoise_Inputs(self)
        self.outputs = KSamplerVariationsWithNoise_Outputs(self)

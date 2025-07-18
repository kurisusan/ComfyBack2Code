
# This file is auto-generated by generate_nodes.py
# Do not edit this file directly.

from ..base_node import Node, InputSlots, OutputSlots, Slot, Model, Conditioning, Latent, Image, Vae, Clip
from typing import Dict, Any, List, Union

# Define input and output slot classes for KSampler_Config__rgthree_
class KSampler_Config__rgthree_Inputs(InputSlots):
    steps_total: Slot[int]
    refiner_step: Slot[int]
    cfg: Slot[float]
    sampler_name: Slot[str]
    scheduler: Slot[str]
    def __init__(self, node: "Node"):
        self.steps_total = Slot[int](node, "steps_total", 'INT')
        self.refiner_step = Slot[int](node, "refiner_step", 'INT')
        self.cfg = Slot[float](node, "cfg", 'FLOAT')
        self.sampler_name = Slot[str](node, "sampler_name", ['euler', 'euler_cfg_pp', 'euler_ancestral', 'euler_ancestral_cfg_pp', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_2s_ancestral_cfg_pp', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_cfg_pp', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ipndm', 'ipndm_v', 'deis', 'res_multistep', 'res_multistep_cfg_pp', 'res_multistep_ancestral', 'res_multistep_ancestral_cfg_pp', 'gradient_estimation', 'gradient_estimation_cfg_pp', 'er_sde', 'seeds_2', 'seeds_3', 'ddim', 'uni_pc', 'uni_pc_bh2'])
        self.scheduler = Slot[str](node, "scheduler", ['simple', 'sgm_uniform', 'karras', 'exponential', 'ddim_uniform', 'beta', 'normal', 'linear_quadratic', 'kl_optimal'])

class KSampler_Config__rgthree_Outputs(OutputSlots):
    steps: Slot[int]
    refiner_step: Slot[int]
    cfg: Slot[float]
    sampler: Slot[str]
    scheduler: Slot[str]
    def __init__(self, node: "Node"):
        self.steps = Slot[int](node, "STEPS", 'INT')
        self.refiner_step = Slot[int](node, "REFINER_STEP", 'INT')
        self.cfg = Slot[float](node, "CFG", 'FLOAT')
        self.sampler = Slot[str](node, "SAMPLER", ['euler', 'euler_cfg_pp', 'euler_ancestral', 'euler_ancestral_cfg_pp', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive', 'dpmpp_2s_ancestral', 'dpmpp_2s_ancestral_cfg_pp', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m', 'dpmpp_2m_cfg_pp', 'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu', 'ddpm', 'lcm', 'ipndm', 'ipndm_v', 'deis', 'res_multistep', 'res_multistep_cfg_pp', 'res_multistep_ancestral', 'res_multistep_ancestral_cfg_pp', 'gradient_estimation', 'gradient_estimation_cfg_pp', 'er_sde', 'seeds_2', 'seeds_3', 'ddim', 'uni_pc', 'uni_pc_bh2'])
        self.scheduler = Slot[str](node, "SCHEDULER", ['simple', 'sgm_uniform', 'karras', 'exponential', 'ddim_uniform', 'beta', 'normal', 'linear_quadratic', 'kl_optimal'])

class KSampler_Config__rgthree_(Node[KSampler_Config__rgthree_Inputs, KSampler_Config__rgthree_Outputs]):
    """
    Original name: KSampler Config (rgthree)
    Category: rgthree
    

    Inputs:
        - steps_total (int) (default: 30)
        - refiner_step (int) (default: 24)
        - cfg (float) (default: 8.0)
        - sampler_name (str)
        - scheduler (str)

    Outputs:
        - steps (int)
        - refiner_step (int)
        - cfg (float)
        - sampler (str)
        - scheduler (str)
    """
    _original_name: str = 'KSampler Config (rgthree)'

    def __init__(self, sampler_name: str, scheduler: str, steps_total: int = 30, refiner_step: int = 24, cfg: float = 8.0):
        super().__init__(**{"steps_total": steps_total, "refiner_step": refiner_step, "cfg": cfg, "sampler_name": sampler_name, "scheduler": scheduler})
        self.inputs = KSampler_Config__rgthree_Inputs(self)
        self.outputs = KSampler_Config__rgthree_Outputs(self)

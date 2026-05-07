"""caideface - MRI defacing pipeline from cai4cai.

A three-step pipeline for anonymising head MRI scans:
1. Reorientation to MNI152 atlas reference (FSL)
2. Skull-stripping with HD-BET and dynamic dilation
3. Affine registration and defacing (BRAINSFit)
"""

__version__ = "0.1.2"

from .pipeline import DefacePipeline
from .reorient import reorient_batch, reorient_single
from .skull_strip import skull_strip_batch, skull_strip_single
from .register import deface_batch, deface_single

__all__ = [
    "DefacePipeline",
    "reorient_batch",
    "reorient_single",
    "skull_strip_batch",
    "skull_strip_single",
    "deface_batch",
    "deface_single",
]

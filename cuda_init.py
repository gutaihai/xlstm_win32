# Copyright (c) NXAI GmbH and its affiliates 2023
# Korbinian Poeppel

import os
from typing import Sequence, Union
import logging
import time
import random
import sys
import torch
#from xlstm.blocks.slstm.src.cpp_ext import load as _load
#from xlstm.blocks.slstm.src.cpp_ext import include_paths
from torch.utils.cpp_extension import load as _load
from torch.utils.cpp_extension import include_paths

LOGGER = logging.getLogger(__name__)
# edit: for windows, you can search for 'edit' to next
IS_WINDOWS = sys.platform == 'win32'
TORCH_HOME = os.path.abspath(torch.__file__).replace('\__init__.py','')
CUDA_HOME=os.environ.get('CUDA_HOME') or os.environ.get('CUDA_PATH')
#


def defines_to_cflags(defines=Union[dict[str, Union[int, str]], Sequence[tuple[str, Union[str, int]]]]):
    cflags = []
    print(defines)
    if isinstance(defines, dict):
        defines = defines.items()
    for key, val in defines:
        cflags.append(f"-D{key}={str(val)}")
    return cflags


curdir = os.path.dirname(__file__)

if torch.cuda.is_available():
    os.environ["CUDA_LIB"] = os.path.join(os.path.split(include_paths(cuda=True)[-1])[0], "lib")


def load(*, name, sources, extra_cflags=(), extra_cuda_cflags=(), **kwargs):
    suffix = ""
    for flag in extra_cflags:
        pref = [st[0] for st in flag[2:].split("=")[0].split("_")]
        if len(pref) > 1:
            pref = pref[1:]
        suffix += "".join(pref)
        value = flag[2:].split("=")[1].replace("-", "m").replace(".", "d")
        value_map = {"float": "f", "__half": "h", "__nv_bfloat16": "b", "true": "1", "false": "0"}
        if value in value_map:
            value = value_map[value]
        suffix += value
    if suffix:
        suffix = "_" + suffix
    suffix = suffix[:64]

    cflags_copy = extra_cflags.copy()
    extra_cflags = list(extra_cflags) + [
        "-U__CUDA_NO_HALF_OPERATORS__",
        "-U__CUDA_NO_HALF_CONVERSIONS__",
        "-U__CUDA_NO_BFLOAT16_OPERATORS__",
        "-U__CUDA_NO_BFLOAT16_CONVERSIONS__",
        "-U__CUDA_NO_BFLOAT162_OPERATORS__",
        "-U__CUDA_NO_BFLOAT162_CONVERSIONS__"
    ]
    
    myargs = {
        "verbose": True,
        "with_cuda": True,
        "extra_ldflags": [
            # edit: don't work on windows, will be replaced
            f"-L{os.environ['CUDA_LIB']}", "-lcublas"
        ],
        "extra_cflags": [*extra_cflags],
        "extra_cuda_cflags": [
            # "-gencode",
            # "arch=compute_70,code=compute_70",
            # "-dbg=1",
            '-Xptxas="-v"',
            "-gencode",
            "arch=compute_80,code=compute_80",
            "-res-usage",
            "--use_fast_math",
            "-O3",
            # edit: '-Xptxas -O3' raise error on windows, will be removed
            "-Xptxas -O3",
            "--extra-device-vectorization",
            *extra_cflags,
            *extra_cuda_cflags,
        ]
    }
    # edit: Test on win11,amd64,VC14.29(VS2019 build tools),
    if IS_WINDOWS:
        myargs = get_args_win32(list(cflags_copy),extra_cuda_cflags)
    print(myargs)
    myargs.update(**kwargs)
    # add random waiting time to minimize deadlocks because of badly managed multicompile of pytorch ext
    time.sleep(random.random() * 10)
    LOGGER.info(f"Before compilation and loading of {name}.")
    mod = _load(name + suffix, sources, **myargs)
    LOGGER.info(f"After compilation and loading of {name}.")
    return mod

def get_args_win32(extra_cflags:list,extra_cuda_cflags):
    r'''
    Transform the args to make it work on the windows
    '''
    win_ldflags = [
        # edit: missing libpath, such as c10.lib
        f"/LIBPATH:{TORCH_HOME}/lib",
        # edit: same as the initial ldflags, but work on windows
        f"/LIBPATH:{CUDA_HOME}/lib/x64","cublas.lib"
    ]
    win_cflags = [
        # edit: include path, such as ATen/ATen.h
        f"-I{TORCH_HOME}/include",
        # edit: include path, such as torch/all.h
        f"-I{TORCH_HOME}/include/torch/csrc/api/include",
        #
        "-U__CUDA_NO_HALF_OPERATORS__",
        "-U__CUDA_NO_HALF_CONVERSIONS__",
        "-U__CUDA_NO_BFLOAT16_OPERATORS__",
        "-U__CUDA_NO_BFLOAT16_CONVERSIONS__",
        "-U__CUDA_NO_BFLOAT162_OPERATORS__",
        "-U__CUDA_NO_BFLOAT162_CONVERSIONS__"
    ]
    win_cflags = extra_cflags + win_cflags
    myargs = {
        "verbose": True,
        "with_cuda": True,
        "extra_ldflags": [*win_ldflags],
        "extra_cflags": [*win_cflags],
        "extra_cuda_cflags": [
            # "-gencode",
            # "arch=compute_70,code=compute_70",
            # "-dbg=1",
            '-Xptxas="-v"',
            "-gencode",
            "arch=compute_80,code=compute_80",
            "-res-usage",
            "--use_fast_math",
            "-O3",
            # edit: '-Xptxas -O3' raise error on windows
            #"-Xptxas -O3",
            "--extra-device-vectorization",
            *win_cflags,
            *extra_cuda_cflags,
        ]
    }
    return myargs
# xlstm_win32
## Usage:<br>
Alternative code for xlstm, make it work on windows. use `cuda_init.py` cover the `(workspacefloder)/xlstm/blocks/slstm/src/cuda_init.py`.<br>
Changes in cuda_init.py were commented, with `edit` in the start of the comments. <br>
Don't forget to use `pip uninstall xlstm` to remove xlstm package in your python enviroment.<br>
## Enviroment:<br>
This is my `build.ninja`:
```
ninja_required_version = 1.3
cxx = cl
nvcc = C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\bin\nvcc

cflags = -DTORCH_EXTENSION_NAME=slstm_HS128BS8NH4NS4DBfDRbDWbDGbDSbDAfNG4SA1GRCV0GRC0d0FCV0FC0d0 -DTORCH_API_INCLUDE_EXTENSION_H -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch\include -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch\include\torch\csrc\api\include -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch\include\TH -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch\include\THC "-IC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\include" -Id:\Program\Anaconda3\envs\xlstm\Include -D_GLIBCXX_USE_CXX11_ABI=0 /MD /wd4819 /wd4251 /wd4244 /wd4267 /wd4275 /wd4018 /wd4190 /wd4624 /wd4067 /wd4068 /EHsc /std:c++17 -DSLSTM_HIDDEN_SIZE=128 -DSLSTM_BATCH_SIZE=8 -DSLSTM_NUM_HEADS=4 -DSLSTM_NUM_STATES=4 -DSLSTM_DTYPE_B=float -DSLSTM_DTYPE_R=__nv_bfloat16 -DSLSTM_DTYPE_W=__nv_bfloat16 -DSLSTM_DTYPE_G=__nv_bfloat16 -DSLSTM_DTYPE_S=__nv_bfloat16 -DSLSTM_DTYPE_A=float -DSLSTM_NUM_GATES=4 -DSLSTM_SIMPLE_AGG=true -DSLSTM_GRADIENT_RECURRENT_CLIPVAL_VALID=false -DSLSTM_GRADIENT_RECURRENT_CLIPVAL=0.0 -DSLSTM_FORWARD_CLIPVAL_VALID=false -DSLSTM_FORWARD_CLIPVAL=0.0 -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch/include -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch/include/torch/csrc/api/include -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_CONVERSIONS__ -U__CUDA_NO_BFLOAT16_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ -U__CUDA_NO_BFLOAT162_OPERATORS__ -U__CUDA_NO_BFLOAT162_CONVERSIONS__
post_cflags = 
cuda_cflags = -Xcudafe --diag_suppress=dll_interface_conflict_dllexport_assumed -Xcudafe --diag_suppress=dll_interface_conflict_none_assumed -Xcudafe --diag_suppress=field_without_dll_interface -Xcudafe --diag_suppress=base_class_has_different_dll_interface -Xcompiler /EHsc -Xcompiler /wd4068 -Xcompiler /wd4067 -Xcompiler /wd4624 -Xcompiler /wd4190 -Xcompiler /wd4018 -Xcompiler /wd4275 -Xcompiler /wd4267 -Xcompiler /wd4244 -Xcompiler /wd4251 -Xcompiler /wd4819 -Xcompiler /MD -DTORCH_EXTENSION_NAME=slstm_HS128BS8NH4NS4DBfDRbDWbDGbDSbDAfNG4SA1GRCV0GRC0d0FCV0FC0d0 -DTORCH_API_INCLUDE_EXTENSION_H -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch\include -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch\include\torch\csrc\api\include -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch\include\TH -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch\include\THC "-IC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\include" -Id:\Program\Anaconda3\envs\xlstm\Include -D_GLIBCXX_USE_CXX11_ABI=0 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -gencode=arch=compute_86,code=compute_86 -gencode=arch=compute_86,code=sm_86 -std=c++17 -Xptxas="-v" -gencode arch=compute_80,code=compute_80 -res-usage --use_fast_math -O3 --extra-device-vectorization -DSLSTM_HIDDEN_SIZE=128 -DSLSTM_BATCH_SIZE=8 -DSLSTM_NUM_HEADS=4 -DSLSTM_NUM_STATES=4 -DSLSTM_DTYPE_B=float -DSLSTM_DTYPE_R=__nv_bfloat16 -DSLSTM_DTYPE_W=__nv_bfloat16 -DSLSTM_DTYPE_G=__nv_bfloat16 -DSLSTM_DTYPE_S=__nv_bfloat16 -DSLSTM_DTYPE_A=float -DSLSTM_NUM_GATES=4 -DSLSTM_SIMPLE_AGG=true -DSLSTM_GRADIENT_RECURRENT_CLIPVAL_VALID=false -DSLSTM_GRADIENT_RECURRENT_CLIPVAL=0.0 -DSLSTM_FORWARD_CLIPVAL_VALID=false -DSLSTM_FORWARD_CLIPVAL=0.0 -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch/include -Id:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch/include/torch/csrc/api/include -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_CONVERSIONS__ -U__CUDA_NO_BFLOAT16_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ -U__CUDA_NO_BFLOAT162_OPERATORS__ -U__CUDA_NO_BFLOAT162_CONVERSIONS__
cuda_post_cflags = 
cuda_dlink_post_cflags = 
ldflags = /DLL /LIBPATH:d:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch/lib "/LIBPATH:C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1/lib/x64" cublas.lib c10.lib c10_cuda.lib torch_cpu.lib torch_cuda.lib -INCLUDE:?warp_size@cuda@at@@YAHXZ torch.lib /LIBPATH:d:\Program\Anaconda3\envs\xlstm\Lib\site-packages\torch\lib torch_python.lib /LIBPATH:d:\Program\Anaconda3\envs\xlstm\libs "/LIBPATH:C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\lib\x64" cudart.lib

rule compile
  command = cl /showIncludes $cflags -c $in /Fo$out $post_cflags
  deps = msvc

rule cuda_compile
  depfile = $out.d
  deps = gcc
  command = $nvcc --generate-dependencies-with-compile --dependency-output $out.d $cuda_cflags -c $in -o $out $cuda_post_cflags



rule link
  command = "D$:\Program\Microsoft Visual Studio\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64/link.exe" $in /nologo $ldflags /out:$out

build slstm.o: compile D$:\Gutaihai\Desktop\xlstm-main\xlstm\blocks\slstm\src\cuda\slstm.cc
build slstm_forward.cuda.o: cuda_compile D$:\Gutaihai\Desktop\xlstm-main\xlstm\blocks\slstm\src\cuda\slstm_forward.cu
build slstm_backward.cuda.o: cuda_compile D$:\Gutaihai\Desktop\xlstm-main\xlstm\blocks\slstm\src\cuda\slstm_backward.cu
build slstm_backward_cut.cuda.o: cuda_compile D$:\Gutaihai\Desktop\xlstm-main\xlstm\blocks\slstm\src\cuda\slstm_backward_cut.cu
build slstm_pointwise.cuda.o: cuda_compile D$:\Gutaihai\Desktop\xlstm-main\xlstm\blocks\slstm\src\cuda\slstm_pointwise.cu
build blas.cuda.o: cuda_compile D$:\Gutaihai\Desktop\xlstm-main\xlstm\blocks\slstm\src\util\blas.cu
build cuda_error.cuda.o: cuda_compile D$:\Gutaihai\Desktop\xlstm-main\xlstm\blocks\slstm\src\util\cuda_error.cu



build slstm_HS128BS8NH4NS4DBfDRbDWbDGbDSbDAfNG4SA1GRCV0GRC0d0FCV0FC0d0.pyd: link slstm.o slstm_forward.cuda.o slstm_backward.cuda.o slstm_backward_cut.cuda.o slstm_pointwise.cuda.o blas.cuda.o cuda_error.cuda.o

default slstm_HS128BS8NH4NS4DBfDRbDWbDGbDSbDAfNG4SA1GRCV0GRC0d0FCV0FC0d0.pyd
```

from setuptools import setup, Extension
import pybind11
from torch.utils.cpp_extension import CppExtension, BuildExtension, library_paths

ext_modules = [
    CppExtension(
        name='norapom',
        sources=['csrc/register_operator.cpp', 'csrc/register_torchscript.cpp'],
        include_dirs=[pybind11.get_include()],
        libraries=['torch'],
        language='c++',
        runtime_library_dirs=library_paths()
    ),
]

setup(
    name='norapom',
    ext_modules=ext_modules,
    cmdclass={
        'build_ext': BuildExtension
    }
)

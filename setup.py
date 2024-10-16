from setuptools import setup, Extension
import pybind11
from torch.utils.cpp_extension import CppExtension, BuildExtension

ext_modules = [
    CppExtension(
        'operators',
        ['csrc/double_operators.cpp', 'csrc/tensor_operators.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++',
    ),
]

setup(
    name='operators',
    ext_modules=ext_modules,
    cmdclass={
        'build_ext': BuildExtension
    }
)

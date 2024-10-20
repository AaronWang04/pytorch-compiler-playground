from setuptools import setup, Extension
import pybind11
from torch.utils.cpp_extension import CppExtension, BuildExtension

ext_modules = [
    CppExtension(
        'COperators',
        ['csrc/operators.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++',
    ),
]

setup(
    name='COperators',
    ext_modules=ext_modules,
    cmdclass={
        'build_ext': BuildExtension
    }
)

from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        'operators',
        ['operators.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++',
    ),
]

setup(
    name='operators',
    ext_modules=ext_modules,
)

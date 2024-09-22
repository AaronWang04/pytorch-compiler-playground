cmake_minimum_required(VERSION 3.4...3.18)

project(compiler)

add_subdirectory(submodules/pybind11)
pybind11_add_module(operators src/operators.cpp)

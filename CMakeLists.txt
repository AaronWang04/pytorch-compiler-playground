cmake_minimum_required(VERSION 3.4...3.18)

project(compiler)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_PREFIX_PATH /submodules/)

find_package(Python3 REQUIRED COMPONENTS Development)
add_subdirectory(submodules/pybind11)
add_subdirectory(submodules/libtorch)

# include(FetchContent)
# FetchContent_Declare(
#     pybind11
#     GIT_REPOSITORY https://github.com/pybind/pybind11.git
#     GIT_TAG v2.10.1
# )
# FetchContent_MakeAvailable(pybind11)

pybind11_add_module(operators csrc/operators.cpp)

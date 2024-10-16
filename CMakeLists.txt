cmake_minimum_required(VERSION 3.4...3.18)

project(compiler)

set(CMAKE_CXX_STANDARD 11)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
add_subdirectory(submodules/pybind11)

execute_process(
  COMMAND ${Python3_EXECUTABLE} -c "import torch; import os; print(os.path.join(torch.__path__[0], 'share', 'cmake', 'Torch'))"
  OUTPUT_VARIABLE Torch_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

# define target
add_library(compiler SHARED csrc/compiler.cpp)

# include(FetchContent)
# FetchContent_Declare(
#     pybind11
#     GIT_REPOSITORY https://github.com/pybind/pybind11.git
#     GIT_TAG v2.10.1
# )
# FetchContent_MakeAvailable(pybind11)

pybind11_add_module(operators csrc/operators.cpp)

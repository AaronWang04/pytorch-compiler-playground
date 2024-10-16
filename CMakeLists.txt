# setup cmake

# cmake version required
cmake_minimum_required(VERSION 3.4...3.18)
# project name
project(cbackend)
# set c++ standard
set(CMAKE_CXX_STANDARD 11)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# define target
add_library(cbackend SHARED csrc/operators.cpp)

add_subdirectory(submodules/pybind11)



target_link_libraries(cbackend PRIVATE pybind11::module)

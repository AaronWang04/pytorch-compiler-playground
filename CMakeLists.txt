# setup cmake

# cmake version required
cmake_minimum_required(VERSION 3.6...3.18)
# project name
project(cbackend)
# set c++ standard
set(CMAKE_CXX_STANDARD 11)

# cmake includes
include(FetchContent)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# define target
add_library(cbackend SHARED csrc/operators.cpp)

# import pybind11
add_subdirectory(submodules/pybind11)

# import libtorch
set(LIBTORCH_VARIANT "cu117")
set(LIBTORCH_VERSION "2.0.1")
set(LIBTORCH_DOWNLOAD_URL "https://download.pytorch.org/libtorch/${LIBTORCH_VARIANT}/libtorch-cxx11-abi-shared-with-deps-${LIBTORCH_VERSION}%2B${LIBTORCH_VARIANT}.zip")
message(STATUS "Downloading libtorch from ${LIBTORCH_DOWNLOAD_URL}")

FetchContent_Declare(
  libtorch
  URL ${LIBTORCH_DOWNLOAD_URL}
)
FetchContent_MakeAvailable(libtorch)

set(Torch_DIR "${libtorch_SOURCE_DIR}/share/cmake/Torch")
find_package(Torch REQUIRED)


target_link_libraries(cbackend PRIVATE pybind11::module)

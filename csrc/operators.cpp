#include <pybind11/pybind11.h> 
#include <torch/extension.h>  // For PyTorch C++ extensions

// Include other source files
#include "double_operators.cpp"
#include "tensor_operators.cpp"

namespace py = pybind11;

PYBIND11_MODULE(COperators, m) {
    // Expose functions
    m.def("tensor_add", &tensor_operators::add, "A function that adds two tensors");
    m.def("tensor_sub", &tensor_operators::subtract, "A function that subtracts two tensors");
    m.def("tensor_mul", &tensor_operators::mul, "A function that multiplies two tensors");
    m.def("tensor_div", &tensor_operators::divide, "A function that divides two tensors");
    m.def("tensor_matmul", &tensor_operators::matmul, "A function that matrix multiplies two tensors");

    m.def("double_add", &double_operators::add, "A function that adds two numbers");
    m.def("double_sub", &double_operators::subtract, "A function that subtracts two numbers");
    m.def("double_mul", &double_operators::mul, "A function that multiplies two numbers");
    m.def("double_div", &double_operators::divide, "A function that divides two numbers");
}
#include "double_operators.cpp"
#include "tensor_operators.cpp"

PYBIND11_MODULE(COperators, m) {
    // expose functions
    m.def("tensor_add", &add, "A function that adds two tensors");
    m.def("tensor_mul", &subtract, "A function that multiplies two tensors");
    m.def("tensor_sub", &mul, "A function that subtracts two tensors");
    m.def("tensor_div", &divide, "A function that divides two tensors");
    m.def("tensor_matmul", &matmul, "A function that matrix multiplies two tensors");

    m.def("double_add", &double_add, "A function that adds two numbers");
    m.def("double_mul", &double_subtract, "A function that multiplies two numbers");
    m.def("double_sub", &double_mul, "A function that subtracts two numbers");
    m.def("double_div", &double_divide, "A function that divides two numbers");
}
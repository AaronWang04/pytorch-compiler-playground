#include <pybind11/pybind11.h>

int add(int i, int j) {
    return i + j;
}

int mul(int i, int j){
    return i * j;
}



PYBIND11_MODULE(operators, m) {
    // expose functions
    m.def("add", &add, "A function that adds two numbers");
    m.def("mul", &mul, "A function that multiplies two numbers");
}

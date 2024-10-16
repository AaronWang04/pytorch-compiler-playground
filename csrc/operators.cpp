#include <pybind11/pybind11.h>

double add(double i, double j) {
    return i + j;
}

double subtract(double i, double j) {
    return i - j;
}

double mul(double i, double j){
    return i * j;
}

double divide(double i, double j){
    return i / j;
}
PYBIND11_MODULE(operators, m) {
    // expose functions
    m.def("add", &add, "A function that adds two numbers");
    m.def("mul", &mul, "A function that multiplies two numbers");
    m.def("subtract", &subtract, "A function that subtracts two numbers");
    m.def("div", &divide, "A function that divides two numbers");
}

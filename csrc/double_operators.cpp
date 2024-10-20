#include <pybind11/pybind11.h>

double double_add(double i, double j) {
    return i + j;
}

double double_subtract(double i, double j) {
    return i - j;
}

double double_mul(double i, double j){
    return i * j;
}

double double_divide(double i, double j){
    return i / j;
}

#include <torch/extension.h>

torch::Tensor add(torch::Tensor i, torch::Tensor j) {
    return i + j;
}

torch::Tensor subtract(torch::Tensor i, torch::Tensor j) {
    return i - j;
}

torch::Tensor mul(torch::Tensor i, torch::Tensor j){
    return i * j;
}

torch::Tensor divide(torch::Tensor i, torch::Tensor j){
    return i / j;
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("add_tensors", &add_tensors, "A function that adds two tensors");
    m.def("mul_tensors", &mul_tensors, "A function that multiplies two tensors");
    m.def("subtract_tensors", &subtract_tensors, "A function that subtracts two tensors");
    m.def("div_tensors", &div_tensors, "A function that divides two tensors");
}

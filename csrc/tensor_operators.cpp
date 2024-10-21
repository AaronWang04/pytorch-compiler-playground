#include <torch/extension.h>  // For PyTorch C++ extensions

namespace tensor_operators {
    
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

    torch::Tensor matmul(torch::Tensor i, torch::Tensor j){
        return i.matmul(j);
    }

}

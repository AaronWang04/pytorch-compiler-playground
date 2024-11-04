// Register torch jit custom passes

#include <pybind11/pybind11.h>
#include <torch/script.h>
#include <torch/extension.h>
#include <ATen/WrapDimUtils.h>
#include <torch/csrc/jit/runtime/custom_operator.h>
#include <torch/csrc/jit/passes/pass_manager.h>
#include <torch/csrc/jit/passes/graph_fuser.h>
#include <torch/csrc/jit/passes/fuse_linear.h>
#include <torch/csrc/jit/passes/fuse_relu.h>
#include <torch/csrc/jit/passes/batch_mm.h>
#include <torch/csrc/jit/ir/ir.h>
#include <torch/csrc/jit/runtime/argument_spec.h>

namespace py = pybind11;
using namespace torch;
using namespace torch::jit;

void register_pass(){
    // Register custom pass
    torch::jit::RegisterPass pass([](std::shared_ptr<Graph> &g){
        FuseAddRelu(g);
        FuseSupportedOps(g);
    }
);
}
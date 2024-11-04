# Notes
Links that helped with learning along the way

https://residentmario.github.io/pytorch-training-performance-guide/intro.html (inspiration)
https://pytorch.org/docs/stable/torch.compiler.html#torch-compiler-overview (reference)
https://github.com/pytorch/pytorch/blob/v1.13.0/torch/csrc/jit/OVERVIEW.md (about torchscript, outdated for dynamo but still relevant for graph representation and pytorch C++ library)
https://jott.live/markdown/Writing%20a%20Toy%20Backend%20Compiler%20for%20PyTorch (outdated but easy to follow compiler explanation)
https://medium.com/@achang67/bring-your-own-compiler-optimization-in-pytorch-5ba8485ca459


Checklist:
- ~~Pybind to import c++ into python~~
- ~~Linking C++ compilation with torch~~
- Writing some c++ operators from scratch rather than use torch's implementation
- Operator fuses passes
- Start with a simple compiler with subgraph compilation
- 

TODO:
- Make tests better, tests are written very poorly, right now its just simple scripts
 
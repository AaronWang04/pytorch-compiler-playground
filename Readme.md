# Pytorch compiler playground
I am currently playing around with how DL compilers work. The goal for this repository is to easily see how different optimization features impact performance. From writing O(n<sup>3</sup>) matmul in native python to using cuda templates, techniques such as operator fusing. This codebase should make it easy to tinker around and see.

## Setup Guide
Prerequisites (for now)
- Python 3.8+

Git
```
git clone https://github.com/AaronWang04/pytorch-compiler-playground.git
git submodule update --init --recursive --remote
```

Create virtual environment
```python
python3 -m venv venv
# on unix
. venv/bin/activate
pip install -r requirements.txt
```

Compile C++
```bash
mkdir build && cd build
cmake ..
make
```

Currently all files are python, you can just run the tests. Soon i'll add for C++ and use pybind as well.
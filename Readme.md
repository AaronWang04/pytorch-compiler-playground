# Pytorch compiler playground
I am currently playing around with how DL compilers work. My goal is to learn all the tooling that enables python and pytorch to work with c++ and cuda. The goal for this repository is to easily see how different optimization features impact performance and to be easy to tinker with. 

## Setup Guide
Prerequisites (for now)
- Python 3.8+

Git repo setup
```
git clone https://github.com/AaronWang04/pytorch-compiler-playground.git
git submodule update --init --recursive --remote
```

Create virtual environment
```python
python3 -m venv venv
source venv/bin/activate # on unix
powershell venv/bin/Activate.ps1 # on WIndows powershell
# you may need to run "Set-ExecutionPolicy Unrestricted"

venv\Scripts\activate.bat # on Windows command prompt
pip install -r requirements.txt
```

### Setup with pip
```bash
python setup.py build
pip install . # or "python setup.py install"
```

### Setup with CMake (Not working right now...)
Build with cmake
```bash
mkdir build && cd build
cmake ..
make
```
You may need to link the build folder
```bash
export PYTHONPATH=$PYTHONPATH:/$(pwd)/build
```

Try and run the pybind tests
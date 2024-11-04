common backend test is ran with
```py
python tests/common_backend_test.py --model matmul --backend python --time
```
model: toy, operator, matmul
backend: toy, python, c
--time to time the execution versus eager
import c_module
from time import time

# Python fib version using recursion
def py_fib(n):
    if (n <= 1):
        return n
    return py_fib(n-1) + py_fib(n-2)

n = 5

# C test
t = time()
c_res = c_module.c_fib(n)
c_time = time() - t

# Python test
t = time()
py_res = py_fib(n)
py_time = time() - t

print(f'Input: {n}\n{py_res=}, {py_time=}\n{c_res=}, {c_time=}')  
import c_module
from time import time

# Python fib version using recursion in python 
def py_fib(x):
    if (x <= 1):
        return x
    return py_fib(x-1) + py_fib(x-2)

x = 5

# C test
t = time()
c_res = c_module.c_fib(x)
c_time = time() - t

# Python test
t = time()
py_res = py_fib(x)
py_time = time() - t

print(f'Input: {x}\n{py_res=}, {py_time=}\n{c_res=}, {c_time=}')  
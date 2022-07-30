// This definition is needed for future-proofing your code
// see https://docs.python.org/3/c-api/arg.html#:~:text=Note%20For%20all,always%20define%20PY_SSIZE_T_CLEAN.
#define PY_SSIZE_T_CLEAN
// The actual Python API
#include <Python.h>
int fib(int n)
{
    if (n<=1)
        return n;
    return fib(n-1) + fib(n-2);

}

PyObject* c_fib(PyObject*self, PyObject*args)
{
    int n;
    PyArg_ParseTuple(args,"i",&n);
    n=fib(n);
    return PyLong_FromLong(n);
}
PyMethodDef module_methods[]=
{
    {"c_fib", c_fib, METH_VARARGS,"method description"},
    {NULL}
};
struct PyModuleDef c_module=
{
    PyModuleDef_HEAD_INIT,
    "c_module",
    "Module description",
    -1,
    module_methods
};

PyMODINIT_FUNC PyInit_c_module()
{
    return PyModule_Create(&c_module);
}
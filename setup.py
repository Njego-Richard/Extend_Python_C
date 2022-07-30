from distutils.core import setup, Extension
#from doctest import Example

#module=Extension("Example", sources=["Example.c"])

#setup(name="packageName",
#version="0.01",
#description="this is a module",
#ext_modules=[module]
#)
module=Extension(
    "c_module",
    ["c_module.c"]
)
setup(
    name="c_module",
    version='1.0',
    description='the package description',
    ext_modules=[module]
)
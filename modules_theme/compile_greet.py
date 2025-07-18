# compile_greet.py
import py_compile

py_compile.compile("greet.py", cfile="__pycache__/greet.pyc")
print("greet.py скомпилирован в __pycache__/greet.pyc")
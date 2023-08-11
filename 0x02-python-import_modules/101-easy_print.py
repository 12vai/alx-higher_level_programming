#!/usr/bin/python3
import builtins
setattr(builtins, "__import__", None)
setattr(builtins, "eval", None)
setattr(builtins, "open", None)
setattr(builtins, "print", lambda x: __import__("sys").stdout.write(x + "\n"))
__import__("sys").stdout.write("#pythoniscool\n")

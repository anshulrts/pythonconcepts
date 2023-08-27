# Scripts vs Modules
# A plain text file containing Python code that is intended to be directly executed by the
# user is usually called script, which is an informal term that means top-level program file.
# On the other hand, a plain text file, which contains Python code that is designed to be imported
# and used from another Python file, is called module.
# So, the main difference between a module and a script is that modules are meant to be imported,
# while scripts are made to be directly executed.


# What’s the Python Interpreter?
# Python is an excellent programming language.
# Python is also a piece of software called an interpreter.
# The interpreter is the program you’ll need to run Python code and scripts.
# Technically, the interpreter is a layer of software that works between your program
# and your computer hardware to get your code running.
# Depending on the Python implementation you use, the interpreter can be:
# A program written in C, like CPython, which is the core implementation of the language
# A program written in Java, like Jython
# A program written in Python itself, like PyPy
# A program implemented in .NET, like IronPython


# The interpreter is able to run Python code in three different ways:
# As a script
# As a module
# As a piece of code typed into an interactive session


# How Does the Interpreter Run Python Scripts?
# When you try to run Python scripts, a multi-step process begins.
# In this process the interpreter will:
# 1. Process the statements of your script in a sequential fashion
# 2. Compile the source code to an intermediate format known as bytecode
# This bytecode is a translation of the code into a lower-level language that’s platform-independent.
# Its purpose is to optimize code execution. So, the next time the interpreter runs your code,
# it’ll bypass this compilation step.
# Strictly speaking, this code optimization is only for modules (imported files), not for
# executable scripts.
# 3. Ship off the code for execution
# At this point, something known as a Python Virtual Machine (PVM) comes into action.
# The PVM is the runtime engine of Python. It is a cycle that iterates over the instructions
# of your bytecode to run them one by one.

# The PVM is not an isolated component of Python. It’s just part of the Python system you’ve installed
# on your machine. Technically, the PVM is the last step of what is called the Python interpreter.
# The whole process to run Python scripts is known as the Python Execution Model.



# What is Python?
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.

# Invoking the Interpreter
The Python interpreter is usually installed as ```/usr/local/bin/python3.10``` on those machines where it is available; putting ```/usr/local/bin``` in your Unix shell’s search path makes it possible to start it by typing the command: 
```python3.10```

# The Zen of Python, by Tim Peters

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
# About PEP-8 (Pycodestyle)
The pycodestyle checker provides code recommendations based on the PEP-8 style conventions. So what exactly is PEP-8?

PEP stands for Python Enhancement Proposal, and PEP-8 is a guide that outlines the best practices of writing Python code. Authored in 2001, its main objective is to improve overall code consistency and readability by standardizing code styles.

One thing to note is that PEP-8 is meant to serve as a guide, and not intended to be interpreted as biblical instructions to always strictly adhere to.

# Features of Pycodestyle
1. Plugin architecture: Adding new checks is easy.
2. Parseable output: Jump to error location in your editor.
3. Small: Just one Python file, requires only stdlib. You can use just the ```pycodestyle.py``` file for this purpose.
4. Comes with a comprehensive test suite.


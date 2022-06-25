# doctest
doctest is a module included in the Python programming language's standard library that allows the easy generation of tests based on output from the standard Python interpreter shell, cut and pasted into docstrings.

# Implementation specifics
Doctest makes innovative use of the following Python capabilities:

1. docstrings
2. The Python interactive shell (both command line and the included idle application)
3. Python introspection

When using the Python shell, the primary prompt: ***>>>*** , is followed by new commands. The secondary prompt: ... , is used when continuing commands on multiple lines; and the result of executing the command is expected on following lines. A blank line, or another line starting with the primary prompt is seen as the end of the output from the command.

The doctest module looks for such sequences of prompts in a docstring, re-executes the extracted command and checks the output against the output of the command given in the docstrings test example.

The default action when running doctests is for no output to be shown when tests pass. This can be modified by options to the doctest runner. In addition, doctest has been integrated with the Python unit test module allowing doctests to be run as standard unittest testcases. Unittest testcase runners allow more options when running tests such as the reporting of test statistics such as tests passed, and failed.

# Doctest — Test interactive Python examples
The *doctest* module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

1. To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
2. To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
3. To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.
Here’s a complete but small example module:
```
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
If you run **example.py** directly from the command line, doctest works its magic:
```
$ python example.py
$
```
There’s no output! That’s normal, and it means all the examples worked. Pass -v to the script, and doctest prints a detailed log of what it’s trying, and prints a summary at the end:
```
$ python example.py -v
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    [factorial(n) for n in range(6)]
Expecting:
    [1, 1, 2, 6, 24, 120]
ok
```
And so on, eventually ending with:

```
Trying:
    factorial(1e100)
Expecting:
    Traceback (most recent call last):
        ...
    OverflowError: n too large
ok
2 items passed all tests:
   1 tests in __main__
   8 tests in __main__.factorial
9 tests in 2 items.
9 passed and 0 failed.
Test passed.
$
```
That’s all you need to know to start making productive use of doctest! Jump in. The following sections provide full details. Note that there are many examples of doctests in the standard Python test suite and libraries.

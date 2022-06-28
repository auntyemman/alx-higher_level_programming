# Python - Everything is object

Python is an object-oriented programming language, and in Python everything is an object.

Let's flesh-out what this means. Earlier we saw that variables are simply pointers, and the variable names themselves have no attached type information. This leads some to claim erroneously that Python is a type-free language. But this is not the case! Consider the following:
```
x = 4
type(x)

int

x = 'hello'
type(x)

str

x = 3.14159
type(x)

float
```
Python has types; however, the types are linked not to the variable names but to the objects themselves.

In object-oriented programming languages like Python, an object is an entity that contains data along with associated metadata and/or functionality. In Python everything is an object, which means every entity has some metadata (called attributes) and associated functionality (called methods). These attributes and methods are accessed via the dot syntax.

For example, before we saw that lists have an append method, which adds an item to the list, and is accessed via the dot (".") syntax:
```
L = [1, 2, 3]
L.append(100)
print(L)

[1, 2, 3, 100]
```

# Background Context

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types. The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.

Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

All answers should be only one line in a file. No space before or after the answer.

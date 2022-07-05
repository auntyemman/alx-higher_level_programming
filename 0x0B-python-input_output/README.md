# Python input/output

Opening Files in Python
Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.
```
>>> f = open("test.txt")    # open file in current directory
>>> f = open("C:/Python38/README.txt")  # specifying full path
```
We can specify the mode while opening a file. In mode, we specify whether we want to read ```r```, write ```w``` or append ```a``` to the file. We can also specify if we want to open the file in text mode or binary mode.

The default is reading in text mode. In this mode, we get strings when reading from the file.

On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.

```
f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
```
Unlike other languages, the character ```a``` does not imply the number 97 until it is encoded using ```ASCII``` (or other equivalent encodings).

Moreover, the default encoding is platform dependent. In windows, it is ```cp1252``` but ```utf-8``` in Linux.

So, we must not also rely on the default encoding or else our code will behave differently in different platforms.

Hence, when working with files in text mode, it is highly recommended to specify the encoding type.

```f = open("test.txt", mode='r', encoding='utf-8')
```

# Closing Files in Python
When we are done with performing operations on the file, we need to properly close the file.

Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.

Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.
```
f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()
```
This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.

A safer way is to use a ***try...finally*** block.
```
try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
```
This way, we are guaranteeing that the file is properly closed even if an exception is raised that causes program flow to stop.

The best way to close a file is by using the ```with``` statement. This ensures that the file is closed when the block inside the ```with``` statement is exited.

We don't need to explicitly call the ```close()``` method. It is done internally.
```
with open("test.txt", encoding = 'utf-8') as f:
   # perform file operations
```

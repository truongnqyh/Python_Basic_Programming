# [expression for item in iterable if condition]

# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)

# Filter even numbers
evens = [x for x in range(100) if x % 2 == 0]
print(evens)

# Lambda arguments: Expression
add = lambda x, y: x + y
print(add(3,5)) # 8

# map() ~ Applies a function to each item in an iterable
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(squares)  # <map object at 0x00000249DE991B10>
print(list(squares)) # [1, 4, 9, 16]

# filter() ~ Filters items based on a condition
evenlist = filter(lambda x: x % 2 == 0, numbers)
print(evenlist)  # <filter object at 0x0000017CE9081C90>
print(list(evenlist)) # [2, 4]

# reduce() ~ Reduces an iterable to a single value
from functools import reduce
product = reduce(lambda x,y: x * y, numbers)
print(product)

# Python's os and sys modules
import os

print(os.getcwd()) # D:\Python\Python_Basic_Programming\Python Basic
# os.mkdir("test_dir") # Create directory
# os.remove("cana.txt") # Clear file

import sys

print(sys.argv)  # ['pythonic_code.py']
print(sys.version) # 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:17:27) [MSC v.1929 64 bit (AMD64)]
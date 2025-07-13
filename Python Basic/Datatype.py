### LIST  -> element can be changed ~ mutable
number = [1, 2, 3, 4]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True]

slice_fruits = fruits[1:3]   # "banana", "cherry"
fruits.append("orange")      # "apple", "banana", "cherry", "orange"
fruits.insert(1, "grape")    # "apple", "grape", "banana", "cherry", "orange"
fruits.remove("apple")       # "grape", "banana", "cherry", "orange"
del fruits[0]                # "banana", "cherry", "orange"
fruits.pop()                 # # "banana", "cherry"

### TUPLES  -> element can not be changed ~ immutable
colors = ("red", "green", "blue")
single_item = ("glass")

print(colors[0])  # "red"
print(colors[-1]) # "blue"

### DICTIONARIES
students = {"name": "Alice", "age": "25", "grade": "A"}

for key, value in students.items():
    print(key, value)

students["subject"] = "Math" # {'name': 'Alice', 'age': '25', 'grade': 'A', 'subject': 'Math'}
students["age"] = "32"       # {'name': 'Alice', 'age': '32', 'grade': 'A', 'subject': 'Math'}
del students["grade"]
students.pop("subject")

### SETS
numbers = {1, 2, 3, 4}
empty_set = set()
numbers.add(8)      # {1, 2, 3, 4, 8}
numbers.remove(2)   # {1, 3, 4, 8}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # {1, 2, 3, 4, 5}
print(set1 & set2)  # {3}
print(set1 - set2)  # {1, 2}

### STRING
first = "Truong"
second = "Com"
result = first + " " + second # Truong Com
text = "Truong Com"
print(text[0:4])
print(text[-5:])
    # Split string
sentence = "Python is good"
words = sentence.split() # ['Python', 'is', 'good']
    # Join string
new_sentence = "|".join(words)  # Python|is|good
text = "i love icecreambaby"
updated_text = text.replace("icecreambaby", "BeKem") # i love BeKem
messy = "    i love BeKem"
new_messy = messy.strip()  # i love BeKem

import re
text = "Contact me at 123-456-das7890"
digits = re.findall(r"\d+", text) # ['123', '456', '7890']
#### re.sub(pattern, repl, text)
updated_text = re.sub(r"\d", "X", text) # Contact me at XXX-XXX-dasXXXX
# r"..." ~ raw string
# Convert string ---> text[start:stop:step]

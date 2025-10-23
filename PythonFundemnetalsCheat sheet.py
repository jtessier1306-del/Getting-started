print("Hello, World!")

name = "Jaden"
age = 25
is_student = True

string_var = "hello"
integer_var = 25
boolean_var = True
float_var = 2.99
list_var = [2, 4, 6, 8, 10]
tuple_var = (123, 456, 789)  # CAN NOT BE CHANGED
dict_var = {"name": "jaden", "age": 25, "is_student": True}

# Basic Operators:
x = 89
print(x + 67)  # 156
print(x - 67)  # 22
print(x * 67)  # 5963
print(x / 67)  # 1.3283582089552238

# Conditionals:
if age >= 18:
    print("You are an Adult")
else:
    print("You are a minor")

# Loops:
for i in range(5):
    print("Inside the loop:", i)
    count = 4
    while count > 0:
        print("Counting down:", count)
        count -= 1
print("Loop ended.")

# Functions:
def greet(jaden):
    return "Hello, " + jaden + "!"
print(greet("jaden"))

# Sets:
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)  # {1, 2, 3, 4, 5, 6}
numbers.remove(3)
print(numbers)  # {1, 2, 4, 5, 6}

# Dictionaries:
person = {"name": "jaden", "age": 25}
print(person["name"])  # jaden
person["age"] = 26
print(person["age"])  # 26
person["Reno"] = "Nevada"
print(person)  # {"name": "jaden", "age": 26, "Reno": "Nevada"}

# Importing Modules:
import math
print(math.sqrt(800))  # 28.284271247461902
import random
print(random.randint(1, 100))  # Random number between 1 and 100


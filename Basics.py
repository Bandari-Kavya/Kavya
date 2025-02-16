# 1. Variables and Data Types
x = 10         # Integer
y = 3.14       # Float
name = "Alice" # String
is_python_fun = True  # Boolean
numbers = [1, 2, 3, 4, 5]  # List
coordinates = (10, 20)  # Tuple
person = {"name": "Alice", "age": 25}  # Dictionary
unique_numbers = {1, 2, 3, 3, 4}  # Set

# 2. Basic Input & Output
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# 3. Conditional Statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# 4. Loops
print("\nFor Loop Example:")
for i in range(5):
    print(i)

print("\nWhile Loop Example:")
count = 0
while count < 3:
    print(count)
    count += 1

# 5. Function
def greet(name):
    return f"Hello, {name}!"

print(greet(user_name))

# 6. Class and Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 25)
print(person1.introduce())

# 7. Exception Handling
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")

# 8. Importing Modules
import math
print(f"Square root of 16 is: {math.sqrt(16)}")

# 9. File Handling
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

with open("example.txt", "r") as file:
    content = file.read()
    print(f"File Content: {content}")

print("Program execution completed!")

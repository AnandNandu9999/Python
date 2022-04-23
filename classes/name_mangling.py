"""
This program will defines the
accessing of private variable
from outside the class
using name Mangling
"""


class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data variable
        self.name = name
        # private data variable
        self.__salary = salary


# creating the object for Employee class
emp = Employee("Jessa", 100000)

# printing Employee name
print(emp.name)

# Accessing the private attribute __salary using name mangling
print("Name:", emp.name, "Salary:", emp._Employee__salary)


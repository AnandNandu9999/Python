"""
This program will defines the
accessing of private variable
from outside the class
using public method
"""


class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data variable
        self.name = name
        # private data variable
        self.__salary = salary

    def show(self):
        print("Name:", self.name, "Salary:", self.__salary)


# creating the object for Employee class
emp = Employee("Jessa", 100000)

# printing Employee name
print(emp.name)

# calling the public method
emp.show()


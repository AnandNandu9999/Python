"""
This Program illustrates the
setter and getter method used
in Encapsulation method to hide the
basic functionality
"""


class Student:
    # constructor
    def __init__(self, name, rollno, age):
        # public data member
        self.name = name
        # private data member
        self.__roll_no = rollno
        # private data member
        self.__age = age

    # Setter method to set the age
    def set_age(self, number):
        self.__age = number

    # getter method to get the age
    def get_age(self):
        return self.__age


# creating an object for the class Student
std = Student("Jessica", 14, 15)

# Printing the age of student using getter method
print("Student age:", std.get_age())

# Setting the age of student using setter method
std.set_age(16)

# Printing the age of student using getter method
print("Student age:", std.get_age())
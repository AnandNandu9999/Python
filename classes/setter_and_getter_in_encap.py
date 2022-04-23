"""
This Program illustrates the
setter and getter method to implement
the Encapsulation method to hide the
background functionality to the user
"""


class Student:
    # constructor
    def __init__(self, name, roll_no, age):
        # public data member
        self.name = name
        # private data member
        self.__roll_no = roll_no
        # private data member
        self.__age = age

    # Setter method to set the age
    def set_age(self, number):
        if number > 50:
            print("Invalid no. Please set the correct age")
        else:
            self.__age = number

    # getter method to get the age
    def get_age(self):
        return self.__age


# creating an object for the class Student
std = Student("Jessica", 14, 15)

# Printing the age of student using getter method
print("Student age:", std.get_age())

# Setting the age of student using setter method with invalid data
std.set_age(56)

# Setting the age of student using setter method with valid data
std.set_age(14)

# Printing the age of student using getter method
print("Student age:", std.get_age())
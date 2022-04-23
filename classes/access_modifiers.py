"""
This program illustrates the access modifiers
in python
"""


class Employee:
    # constructor
    def __init__(self, name, salary, age):
        """
        :param name: Name of the employee as public member
        :param salary: Salary of the employee as protected member
        :param age: Age of the employee as private member
        """
        # public data variable
        self.name = name
        # protected data variable
        self._salary = salary
        # private data variable
        self.__age = age

    # public method
    def show(self):
        print("Name:", self.name, "Salary:", self._salary, "Age", self.__age)


# creating an object for the class Employee
emp = Employee("Jessica", 100000, 24)

# calling the public method using object "emp"
emp.show()

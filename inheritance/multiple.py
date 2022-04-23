"""
This program illustrates the multiple
inheritance concept
"""


class Hardware:
    # constructor
    def __init__(self, soc, subsytem):
        # public data members
        self.soc = soc
        self.subsystem = subsytem


class Software:
    # constructor
    def __init__(self, error, version):
        # public data members
        self.error = error
        self.version = version


# inheriting the Hardware and Software
class Product(Hardware, Software):
    def __init__(self, soc, subsystem, error, version):
        Hardware.__init__(self, soc, subsystem)
        Software.__init__(self, error, version)

    def display(self):
        print(self.soc, self.subsystem, self.error, self.version)


# creating an object for the class Product
Device = Product("90nm", "ADSP", "watchdgbite", "Android12")

# printing the hardware and software information in product class
Device.display()

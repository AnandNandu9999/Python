a = "global a"


class Main:
    def __init__(self):
        pass

    # outer function
    def outer(self):
        a = "outer a"

        # inner function
        def inner():
            a = "inner a"
            print(a)

        print(a)
        inner()


a = "main a"
print(a)
# creating an object for the class Main
obj = Main()
# calling the method "outer" of "Main" class
obj.outer()

# printing the value of a
print(a)
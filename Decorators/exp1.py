"""
https://www.youtube.com/watch?v=FsAPt_9Bf3U
"""


def outer_function():
    msg = "Hello"

    def inner():
        print(msg)

    # executes the inner method
    return inner()
    # returns the object of inner method
    # return inner


def outer(msg):
    msg = msg

    def inner():
        print(msg)

    return inner


def decorator_function(msg):
    def wrapper_function():
        print(msg)
    return wrapper_function


# obj = outer_function()
# obj()
obj1 = outer("Hello1")
obj1()

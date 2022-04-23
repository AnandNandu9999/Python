class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    # same as wrapper function in function decorators
    def __call__(self, *args, **kwargs):
        print('wrapper executed before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display(name, age):
    print("Executed the display function")
    print("Name is:", name, "Age is:", age)


display("Anand", "24")



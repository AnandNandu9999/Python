def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display(name, age):
    print("Executed the display function")
    print("Name is:", name, "Age is:", age)


display("Anand", "24")

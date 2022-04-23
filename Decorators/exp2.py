from functools import wraps


def my_logger(org_func):
    import logging
    logging.basicConfig(filename="{}.log".format(org_func.__name__), level=logging.INFO)

    @wraps(org_func)
    def wrapper(*args, **kwargs):
        logging.info("Executed with args: {}, Kwargs: {}".format(args, kwargs))
        return org_func(*args, **kwargs)
    return wrapper


def timer(org_func):
    import time

    @wraps(org_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = org_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} function ran in {}".format(org_func.__name__, t2))
        return result
    return wrapper


@my_logger
@timer
# @my_logger
def display(name, age):
    import time
    # time.sleep(5)
    print("Executed the display function")
    print("Name is:", name, "Age is:", age)


display("Anand", "24")

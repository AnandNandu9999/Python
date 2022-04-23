a = "global a"


def outer():
    # by the keyword global it will
    # modify the value in globally also
    global a
    a = "outer a"

    def inner():
        # value will not be changed
        # as it is local to inner function
        a = "inner a"
        print(a)

    print(a)
    inner()


a = "main a"
print(a)
outer()
print(a)

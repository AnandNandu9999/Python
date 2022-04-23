a = "global a"


def outer():
    a = "outer a"

    def inner():
        # by the keyword global it will
        # modify the value in globally also
        global a
        a = "inner a"
        print(a)

    print(a)
    inner()


a = "main a"
print(a)
outer()
print(a)

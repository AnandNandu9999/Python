
def outer():
    a = "outer a"

    def inner():
        nonlocal a
        a = "inner a"
        print(a)

    inner()
    print(a)


a = "main a"
print(a)
outer()
print(a)

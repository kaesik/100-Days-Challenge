def outer_fun():
    print("Outer function")

    def inner_fun():
        print("Inner function")

    return inner_fun()

outer_fun()

def decorator_fun(func):
    def wrapper_fun():
        print("Wrapper function")
        func()
    return wrapper_fun

def say_hello():
    print("Hello")
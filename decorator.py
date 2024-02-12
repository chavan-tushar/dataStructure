def add_decorator(function_name):

    def wrap_func(a, b):
        sub = a - b
        mul = a * b
        add = function_name(a, b)
        div = a // b
        return add, sub, mul, div
    return wrap_func

@add_decorator
def addition(a, b):
    return a+b


if hasattr(addition, '__wrapped__') or addition.__name__ not in globals():
    add, sub, mul, div = addition(1,2)
    print(f"Addition is {add}, Sub is {sub}, Mul is {mul}, Div is {div}")
else:
    add = addition(1,2)
    print(f"Addition is {add}")

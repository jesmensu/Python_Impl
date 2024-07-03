# ORIGINAL FUNCTION
def division(a, b):
    return a/b
# DECORATOR FUNCTION
def smart_div(func):
    def inner(a,b):
        if b == 0:
            raise ValueError("Can't divide by zero")
        else:
            return func(a,b)
    return inner

# # Normal traditional process
# division = smart_div(division)
# # CALL THE FUNCTION
# result = division(6,4)
# print(result)

# Decorator function using @ symbol
@smart_div
def division(a, b):
    return a/b
division(4,2)






def add_event(func):
    def inner(a,b):
        if a%2 == 1 or b%2 == 1:
            return "We are only adding even values"
        else:
            return func(a,b)
    return inner

@add_event
def add(a,b):
    return a+b

print(add(3,2))


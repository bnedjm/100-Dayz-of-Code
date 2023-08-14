# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(F"You called {function.__name__}({args[0]}, {args[1]}, {args[2]})")
        print(f"It returned: {function(args[0], args[1], args[2])}") 
    return wrapper

# Use the decorator 👇

@logging_decorator
def add(a, b, c):
    return a+b+c

add(1,2,3)

# Understanding decorators

from functools import wraps


def my_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Before function execution")

        result = function(*args, **kwargs)

        print("After function execution")
        return result

    return wrapper


@my_decorator
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeting sent to {name}"


message = greet("Madan")

print(message)

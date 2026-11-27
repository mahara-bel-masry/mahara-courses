def log_call(func):
    def wrapper(*args):
        print("calling", func.__name__)
        return func(*args)
    return wrapper


@log_call
def add(a, b):
    return a + b


print(add(2, 3))

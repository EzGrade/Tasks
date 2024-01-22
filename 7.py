def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"add(3, 4) was called and returned {result}")

    return wrapper


@debug
def add(a, b):
    return a + b


add(3, 4)

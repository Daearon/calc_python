def summarize(a, b):
    return a + b


def subtract(a, b):
    return a - b


def product(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Деление на ноль невозможно")



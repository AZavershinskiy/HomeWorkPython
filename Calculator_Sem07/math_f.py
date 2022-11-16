def equation(string, a, b):
    if string == '+':
        return summ(a, b)
    elif string == '-':
        return subtraction(a, b)
    elif string == '*':
        return multiply(a, b)
    elif string == '/':
        return division(a, b)


def summ(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b

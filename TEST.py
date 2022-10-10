# Для теста кода


x = 5
y = 3


def calc(a, b):
    global x
    global y
    x = a
    y = b


def summ():
    return x + y


print(summ())
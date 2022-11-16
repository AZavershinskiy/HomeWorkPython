def number_request():
    return int(input('Введите число: '))


def operation_request():
    return input('Введите действие (+, -, *, /): ')


def output(a, b, operator, result):
    print(f'{a} {operator} {b} = {result}')

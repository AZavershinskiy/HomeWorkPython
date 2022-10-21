# Вычислить число Пи c заданной точностью d
# при $d = 0.001, π = 3.141


from math import pi


def precision_calculation_pi(d):
    text = str(pi)
    return float(text[:len(d)])


d = input('Задайте точность определения числа Пи (например: 0.001): ')
print(f'{precision_calculation_pi(d)} - вычисленное число Пи без округления с точностью: {d}')

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def polynomial(degree):
    polynomial_notation = ''
    for i in range(degree + 1):
        num = randint(0, 100)
        if num != 0:
            if i < (degree - 1):
                polynomial_notation += f'{num}*x^{degree - i} + '
            elif i == (degree - 1):
                polynomial_notation += f'{num}*x + '
            else:
                polynomial_notation += f'{num} = 0'
    return polynomial_notation


degree = int(input('Введите значение натуральной степени: '))
with open("Polynomials.txt", 'a') as file:
    file.write(f'\n{polynomial(degree)}')

print(f'Многочлен {degree} степени записан в файл "Polynomials.txt"')

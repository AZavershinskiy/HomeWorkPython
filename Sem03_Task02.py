# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from math import ceil


def product_nums(list1):
    product_list = []
    for i in range(ceil(len(list1)/2)):
        product = list1[i] * list1[len(list1) - i - 1]
        product_list.append(product)
    return product_list


list_nums = [int(i) for i in input(
    'Введите список из нескольких чисел через пробел: ').split()]
print(f'{list_nums} - получившийся список')
print(f'{product_nums(list_nums)} - произведение пар чисел списка')

# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

from audioop import reverse


def fib_list(n):
    list1 = []
    list2 = []
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
        list1.append(first)
    for i in range(len(list1)):
        if i % 2 != 0:
            list2.append(list1[i] * -1)
        else:
            list2.append(list1[i])
    list2.reverse()
    list2.append(0)
    for i in range(len(list1)):
        list2.append(list1[i])
    return list2


n = int(input('Введите число: '))
print(
    f'Список чисел Фибоначчи, в том числе для отрицательных индексов, числа {n}:\n{fib_list(n)}')
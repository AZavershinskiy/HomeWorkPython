# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значениями дробной части элементов.

def diff_min_max(list1):
    list2 = []
    for i in list1:
        round_value = 0
        x = str(i).split('.')
        size = len(x[1])
        if size > round_value:
            round_value = size
        n = i % 1
        list2.append(round(n, round_value))
    diff = max(list2) - min(list2)
    return diff


list_nums = [float(i) for i in input(
    'Введите список из нескольких вещественных чисел через пробел: ').split()]
print(f'{list_nums} - получившийся список')
print(f'{diff_min_max(list_nums)} - разница между максимальным и минимальным '
      'значениями дробной части элементов списка')
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint

res = 1
list2 = []
text = input('Введите размер списка затем индексы элементов, '
             'которые нужно перемножить, через пробел: ').split()
list = [int(i) for i in text]
for i in range(-list[0], list[0], 2):
    list2.append(randint(-list[0], list[0]))
print(f'{list2} - получившийся список')
for i in list[1:]:
    if list[0] <= i:
        print(
            f'Ошибка! Введенный индекс со значением  "{i}" должен быть меньше размера списка: {list[0]}')
        break
    else:
        res *= list2[i]
print(f'{res} - произведение заданных индексов')


# Нужно исправить под задание с файлом!!!
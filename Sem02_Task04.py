# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint


list_positions = []
with open('Item_positions.txt', 'r') as my_file:
    for i in my_file:
        list_positions.append(int(i))
list_positions.sort()
print(f'{list_positions} - список позиций элементов из файла '
      'для нахождения их произведения')
n_list = []
for i in range(max(list_positions) + 1):
    n_list.append(randint(-max(list_positions), max(list_positions)))
print(f'\n{n_list} - получившийся список')
res = 1
for i in list_positions:
    res *= n_list[i]
print(f'\n{res} - произведение заданных элементов')

# в нашем случае N элемент - это максимальное значение индекса (8)
# из файла позиций (Item positions.txt)

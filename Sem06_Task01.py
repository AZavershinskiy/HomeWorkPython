# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

""" 
def Sum_Odd_Nums(list1):
    sum1 = 0
    for i in range(len(list1)):
        if i % 2 != 0:
            sum1 += list1[i]
    return sum1


list_nums = [int(i) for i in input(
    'Введите список из нескольких чисел через пробел: ').split()]
print(f'{list_nums} - получившийся список')
print(f'{Sum_Odd_Nums(list_nums)} - сумма элементов списка нечетных позиций')
 """

# list comprehension
user_list = [1, 2, 3, 4, 5]
res = sum([user_list[i] for i in range(0, len(user_list), 2)])
print(f'{res} -> сумма элементов списка: {user_list}, - на нечетных позициях')
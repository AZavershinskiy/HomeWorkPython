# Для теста кода


# def f(x):
#     return x**2


# list1 = [(i, f(i)) for i in range(2, 11, 2)]
# print(list1)  # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000)]


# list1 = []
# with open('Test.txt', 'r') as test_file:
#     data = test_file.read().split()
#     for i in data:
#         if not int(i) % 2:
#             list1.append((int(i), int(i)**2))
# print(list1)  # [(2, 4), (4, 16), (6, 36), (8, 64)]


# fructs = ['яблоко', 'груша', 'банан', 'апельсин']
# my_list = list(filter(lambda x: len(x) <= 5, fructs))
# print(my_list)  # ['груша', 'банан']


# fructs = ['яблоко', 'груша', 'банан', 'апельсин']
# my_list = list(enumerate(fructs))
# print(my_list)  # [(0, 'яблоко'), (1, 'груша'), (2, 'банан'), (3, 'апельсин')]


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# fructs = ['яблоко', 'груша', 'банан', 'апельсин']
# my_list = list(zip(fructs, nums))
# print(my_list)  # [('яблоко', 1), ('груша', 2), ('банан', 3), ('апельсин', 4)]


# my_dict = {}
# n = 6
# for i in range(1, n+1):
#     my_dict[i] = 3 * i + 1
# print(my_dict)  # {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# print(bin(14)[2:])  # 1110 - 14 в двоичной


# koefs = [-1, 0, 1, 2, 3]
# new_dict = dict(enumerate(koefs))
# print(new_dict[0])  # -1



# A[i] - 1 = A[i-1]
# 1 2 3 4 5 6 8 9

# with open('test.txt', 'r') as file:
#     a = list(map(int, file.read().split()))
#     for i in range(len(a)-1):
#         if a[i]+1 != a[i+1]:
# print(a[i]+1)  # 7


# list1 = [1, 2, 3, 4, 5]
# list2 = [9, 0, *list1]

# print(list2)  # [9, 0, 1, 2, 3, 4, 5]
# print(list2[-1])  # 5



# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности 

# from itertools import count

# list1 = [1, 2, 2, 2, 5, 5, 6, 8, 9, 9, 10]
# list2 = []

# for i in range(len(list1)-1):
#     if list1.count(i) == 1:
#         list2.append(i)
# print(list2)  # [1, 6, 10]

# import re

# st = 'Привет, мой друг! Как поживваешь?'
# list1 = re.split(', | ', st)
# print(list1)  # ['Привет', 'мой', 'друг!', 'Как', 'поживваешь?']



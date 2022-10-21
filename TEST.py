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


print(round(199, -1))
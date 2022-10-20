# Реализуйте алгоритм перемешивания списка.


from random import randint, shuffle


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f'{list1} - исходный список')
# shuffle(list1)
# print(f'\n{list1} - перемешанный список')


""" или """


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'{list1} - исходный список')
index_list = []
list2 = []
while len(index_list) != len(list1):
    index = randint(0, len(list1) - 1)
    if not (index in index_list):
        index_list.append(index)
for i in index_list:
    list2.append(list1[i])
print(f'\n{list2} - перемешанный список')

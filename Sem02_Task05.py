# Реализуйте алгоритм перемешивания списка.


from random import randint, shuffle

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'{list} - исходный список')
shuffle(list)
print('---')
print(f'{list} - перемешанный список')
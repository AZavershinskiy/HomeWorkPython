# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from math import ceil

""" 
def Product_Nums(list1):
    product_list = []
    for i in range(ceil(len(list1)/2)):
        product = list1[i] * list1[len(list1) - i - 1]
        product_list.append(product)
    return 


list_nums = [int(i) for i in input(
    'Введите список из нескольких чисел через пробел: ').split()]
print(f'{list_nums} - получившийся список')
print(f'{Product_Nums(list_nums)} - произведение пар чисел списка')
 """

# list comprehension and map
list_nums = list(map(int, input('Введите список из нескольких чисел через пробел: ').split()))
product_list = [(list_nums[i] * list_nums[len(list_nums) - i - 1])for i in range(ceil(len(list_nums)/2))]
print(f'{product_list} -> произведение пар чисел из списка: {list_nums}')
# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности

# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


def unique_elements(nums_list):
    result_list = []
    for i in nums_list:
        if nums_list.count(i) == 1:
            result_list.append(i)
    return result_list


nums_list = [1, 1, 2, 3, 4, 5, 5]
print(unique_elements(nums_list))

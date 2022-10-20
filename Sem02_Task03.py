# Задайте список из k чисел последовательности (1 + 1 / k) ^ k и выведите на экран их сумму.

list = []
sum = 0
k = int(input('Введите число k: '))
for i in range(1, k+1):
    list.append((1 + 1 / i) ** i)
print(f'{list} - получившийся список')
for i in list:
    sum += i
print(f'{round(sum, 2)} - сумма элементов списка (с округлением)')

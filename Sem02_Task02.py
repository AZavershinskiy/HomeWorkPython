# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


n = int(input('Введите число: '))
f = 1
nums = []
for i in range(1, n+1):
    nums.append(f * i)
print(*nums, sep=', ')

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


# n = input('Введите вещественное число: ')
# x = n.split(".")
# a = int(x[0])
# b = int(x[1])
# sum = 0
# while a != 0:
#     sum += a % 10
#     a //= 10
# while b != 0:
#     sum += b % 10
#     b //= 10
# print(f'Сумма цифр равна: {sum}')


""" или """


n = input('Введите вещественное число: ')
sum = 0
for i in n:
    if i.isdigit():
        sum += int(i)
print(f'Сумма цифр равна: {sum}')
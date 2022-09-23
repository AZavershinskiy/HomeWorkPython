# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]


def prime_factors(n):
   i = 2
   list1 = []
   while i * i <= n:
       while n % i == 0:
           list1.append(i)
           n /= i
       i += 1
   if n > 1:
       list1.append(int(n))
   return list1


n = int(input('Введите натуральное число: '))
print(prime_factors(n))
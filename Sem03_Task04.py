# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def Dec_To_Bin(dec):
    bin = ''
    while dec > 0:
        bin = str(dec % 2) + bin
        dec //= 2
    return bin


dec = int(input('Введите десятичное число: '))
print(f'Преобразовнное десятичное число {dec} в двоичное: {Dec_To_Bin(dec)}')
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def dec_to_bin(dec):
    bin = ''
    while dec > 0:
        bin = str(dec % 2) + bin
        dec //= 2
    return bin


dec = int(input('Введите десятичное число: '))
print(f'Преобразовнное десятичное число {dec} в двоичное: {dec_to_bin(dec)}')

# Напишите программу, которая по заданному номеру четверти показывает
# диапазон возможных координат точек в этой четверти (x и y).


n = int(input('Введите № четверти: '))
if n == 1:
    print(f'В четверти №1 координаты: X > 0,  Y > 0')
elif n == 2:
    print(f'В четверти №2 координаты: X < 0,  Y > 0')
elif n == 3:
    print(f'В четверти №3 координаты: X < 0,  Y < 0')
elif n == 4:
    print(f'В четверти №4 координаты: X > 0,  Y < 0')
else:
    print('Ошибка! Четвертей всего 4!')
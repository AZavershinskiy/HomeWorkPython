# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


from random import randint


diap = (0, 1)
for x in diap:
    for y in diap:
        for z in diap:
            left_side = not (x or y or z)
            right_side = not x and not y and not z
            print(x, y, z, left_side == right_side)
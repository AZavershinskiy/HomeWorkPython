# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


from random import randint

x = randint(0, 10)
y = randint(0, 10)
z = randint(0, 10)
print(f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\nX={x}\nY={y}\nZ={z}')
print(not (x or y or z) == (not x and not y and not z))
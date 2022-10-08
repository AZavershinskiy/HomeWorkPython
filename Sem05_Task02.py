# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint
import time


def player_turn(player, leftover_candy, difficulty=0):
    if player == 'ИИ':
        if difficulty == 1:
            return easy_AI(leftover_candy)
        return hard_AI(leftover_candy)
    else:
        while True:
            user_candy = input(f'Ход игрока {player}: ')
            if user_candy.isdigit():
                if 0 < int(user_candy) < 29:
                    return int(user_candy)
                else:
                    print('За один ход можно забрать от 1 до 28 конфет')
            else:
                print('Введите корректное количество конфет!')


def user_name(number_user):
    if number_user == 0:
        return input('Введите Ваше имя: ')
    elif number_user == 1:
        return input('Введите имя первого игрока: ')
    return input('Введите имя второго игрока: ')


def easy_AI(leftover_candy):
    if leftover_candy > 28:
        return randint(1, 28)
    else:
        return randint(1, leftover_candy + 1)


def hard_AI(leftover_candy):
    if leftover_candy > 56:
        if leftover_candy % 28 == 0:
            return randint(1, 28)
        return leftover_candy % 28
    elif 29 < leftover_candy <= 56:
        return leftover_candy - 29
    elif leftover_candy == 29:
        message1 = '\nИИ: "Ух ты! Кажется, ИИ обыгран, штош, сделаю свой последний ход ¯\_(ツ)_/¯"\n\n'
        for i in message1:
            print(i, end='', flush=True)
            time.sleep(0.03)
        return randint(1, 28)
    else:
        message2 = '\nИИ: "Лол =D"\n\n'
        for i in message2:
            print(i, end='', flush=True)
            time.sleep(0.05)
        return leftover_candy


sweets = 2021
choice_move = randint(0, 1)

print("""ЗДРАВСТВУЙТЕ!
    Это игра КОНФЕТКИ
Правила:
    На столе лежит 2021 конфета
    За ход можно забрать от 1 до 28 конфет
    Выигрывает тот, кто забрал последние конфеты!
Режимы игры:
    1 - Игра с другом
    2 - Игра против ИИ\n""")

opponent = int(input('C кем играть: '))
user_1 = (user_name(1) if opponent == 1 else user_name(0))
user_2 = (user_name(2) if opponent == 1 else 'ИИ')

if opponent != 1:
    difficulty = int(input('''Выбор сложности: 
        1 - Легко
        2 - Сложно
            Выбор: '''))

while sweets > 0:
    if opponent == 2:
        if difficulty == 1:
            AI_turn = player_turn(
                user_1 if choice_move else user_2, sweets, difficulty)
        else:
            AI_turn = player_turn(
                user_1 if choice_move else user_2, sweets, difficulty)
        if not(choice_move):
            print(f'Ход ИИ: {AI_turn}')
        sweets -= AI_turn
    else:
        sweets -= player_turn(user_1 if choice_move else user_2, sweets)
    choice_move = not choice_move
    print(f'Количество конфет = {sweets}')
else:
    print(f'Победил(а): {user_2 if choice_move else user_1}!')
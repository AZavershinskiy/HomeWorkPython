import csv
import db
from prettytable import prettytable


def get_new_id():
    with open(db.file_path, 'r') as file:
        contact_new_id = len(file.readlines())
        return contact_new_id


def show_contacts():
    with open(db.file_path, mode="r", encoding='utf-8') as file:
        table = prettytable.from_csv(file)
        print(table)


def adds_new():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    note = input('Введите примечание к контакту: ')
    with open(db.file_path, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator='\r')
        file_writer.writerow(
            [get_new_id(),
             first_name,
             last_name,
             phone, note])
    print('Готово! Контакт добавлен')


def editor():
    with open(db.file_path, mode="r+", encoding='utf-8') as file:
        search_id = int(input('Введите ID изменяемого контакта: '))
        table = prettytable.from_csv(file)
        table = table.get_string(start=search_id-1, end=search_id)
        print(table)
        


def finder():
    with open(db.file_path, mode="r", encoding='utf-8') as file:
        check = input("""Вам известен ID контакта?
            1 - ДА
            2 - НЕТ
        Ответ: """)
        if check == '1':
            search_id = int(input('Введите ID: '))
            table = prettytable.from_csv(file)
            table = table.get_string(start=search_id-1, end=search_id)
            print(table)
        elif check == '2':
            search_word = input('\nОбщий поиск: ').lower()
            file.readline()
            for row in file:
                if search_word in row.lower():
                    search_id = int(row[0])
                    table = prettytable.from_csv(file)
                    table = table.get_string(start=search_id-1, end=search_id)
                    print(table)
                elif not (search_word in row.lower()):
                    print('Извините! Ничего не найдено\n')
                    continue

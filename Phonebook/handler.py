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
    with open(db.file_path, 'r', encoding='utf-8') as file:
        search_id = int(input('Введите ID изменяемого контакта: '))
        table = prettytable.from_csv(file)
        table = table.get_string(start=search_id-1, end=search_id)
        print(table)
    input_field = int(input("""Какое поле редактировать?
        1 - Имя
        2 - Фамилия
        3 - Телефон
        4 - Примечание
 Ответ: """))
    new_value = input('Введите новое значение: ')
    dialect_params = dict(delimiter=';')
    with open(db.file_path, 'r+', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, **dialect_params)
        lines = []
        for current_line in reader:
            if reader.line_num == search_id+1:
                current_line[input_field] = new_value
            lines.append(current_line)
        file.seek(0)
        csv.writer(file, **dialect_params).writerows(lines)
        file.truncate()
        print('Готово! Запись изменена:')
    with open(db.file_path, mode="r", encoding='utf-8') as file:
        table = prettytable.from_csv(file)
        table = table.get_string(start=search_id-1, end=search_id)
        print(table)


def finder():
    with open(db.file_path, 'r', encoding='utf-8') as file:
        csv.Sniffer().sniff(file.readline())
        answer = input("""Вам известен ID контакта?
            1 - ДА
            2 - НЕТ
        Ответ: """)
        if answer == '1':
            search_id = int(input('Введите ID: '))
            table = prettytable.from_csv(file)
            table = table.get_string(start=search_id-1, end=search_id)
            print(table)
        if answer == '2':
            search_word = input('\nПоиск по всей базе: ').lower()
            for row in file:
                if search_word in row.lower():
                    search_id = int(row[0])
                    table = prettytable.from_csv(file)
                    table = table.get_string(start=search_id-1, end=search_id)
                    print(table)

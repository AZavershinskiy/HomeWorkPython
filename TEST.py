# Для теста кода
import csv


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

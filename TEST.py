# Для теста кода
import csv


def finder():
    with open(db.file_path, mode='r', encoding='utf-8') as file:
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
        elif answer == '2':
            search_word = input('\nПоиск: ').lower()
            for row in file:
                if search_word in row.lower():
                    search_id = int(row[0])
                    table = prettytable.from_csv(file)
                    table = table.get_string(start=search_id-1, end=search_id)
                    print(table)

# возможно, проблема в Win7
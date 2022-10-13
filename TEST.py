# Для теста кода
import csv


def update_csv_cell(address, new_value):
    filepath = 'phonebook/base.csv'
    dialect_params = dict(delimiter=';')
    col_num, row_num = address
    with open(filepath, 'r+', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, **dialect_params)
        lines = []
        for current_line in reader:
            if reader.line_num == row_num:
                current_line[col_num-1] = new_value
            lines.append(current_line)
        file.seek(0)
        csv.writer(file, **dialect_params).writerows(lines)
        file.truncate()
        print('ГОТОВО!')


update_csv_cell(address=(5, 7+1), new_value='НОВЫЙ ТЕКСТ')

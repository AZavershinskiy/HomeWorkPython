from msilib.schema import Control
import csv
import db


def get_new_id():
    file = open('phonebook/base.csv')
    contact_new_id = len(file.readlines())
    return contact_new_id


def adds_new():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    note = input('Введите примечание к контакту: ')
    with open(db.base_contacts, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(
            [get_new_id(), first_name, last_name, phone, note])

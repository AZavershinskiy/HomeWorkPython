from prettytable import prettytable
import db


def show_contacts():
    with open(db.base_contacts, 'r') as input_base:
        table = prettytable.from_csv(input_base)
        return table
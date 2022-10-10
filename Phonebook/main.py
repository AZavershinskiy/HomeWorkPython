import control

dict_fieldnames = {1: 'Имя', 2: 'Фамилия', 3: 'Телефон', 4: 'Примечание'}
fieldnames = ['id', 'Имя', 'Фамилия', 'Телефон', 'Примечание']

path = 'Phonebook/base.csv'
control.work(path, dict_fieldnames, fieldnames)
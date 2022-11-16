def saving_numbers(a, b, operation):
    path = 'Sem07_Сalculator/numbers.txt'
    with open(path, 'a') as file:
        file.write(f'{a}{operation}{b}\n')


def reading_number():
    path = 'Sem07_Сalculator/numbers.txt'
    with open(path, 'r') as file:
        return file.readlines()[-1]

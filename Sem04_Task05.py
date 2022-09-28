# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def getting_list_functions(file_name):
    with open(f'{file_name}', 'r') as file:
        polynomials = file.read().split('\n')
    for i in range(len(polynomials)):
        polynomials[i] = polynomials[i].replace(' = 0', '').split(' + ')
        for k in range(len(polynomials[i])):
            polynomials[i][k] = polynomials[i][k].split('*')
    return polynomials


def write_to_file(name_file, text):
    with open(f'{name_file}', 'a') as file:
        file.write(f'{text}\n')


def sum_polynomials(polynomials_1, polynomials_2):
    polynomials_max_len = polynomials_1
    polynomials_min_len = polynomials_2
    if polynomials_1 < polynomials_2:
        polynomials_max_len = polynomials_2
        polynomials_min_len = polynomials_1
    result = ''
    for i in range(len(polynomials_max_len)):
        if len(polynomials_max_len[i]) != 1:
            for k in range(len(polynomials_min_len)):
                if len(polynomials_min_len[k]) != 1:
                    if polynomials_max_len[i][1] == polynomials_min_len[k][1]:
                        result += f'{int(polynomials_max_len[i][0]) + int(polynomials_min_len[k][0])}*{polynomials_max_len[i][1]}'
                        break
                elif (k == len(polynomials_min_len) - 1):
                    result += f'{polynomials_max_len[i][0]}*{polynomials_max_len[i][1]}'
        else:
            for k in range(len(polynomials_min_len)):
                if len(polynomials_min_len[k]) == 1:
                    result += f'{int(polynomials_max_len[i][0])+ int(polynomials_min_len[k][0])}'
        if i != (len(polynomials_max_len) - 1):
            result += ' + '
    return result + ' = 0'


polynomials_1 = getting_list_functions('Polynomials_file1.txt')
polynomials_2 = getting_list_functions('Polynomials_file2.txt')

new_polynomials = []
for i in range(len(polynomials_1)):
    new_polynomials.append(sum_polynomials(polynomials_1[i], polynomials_2[i]))

for i in new_polynomials:
    write_to_file('Sum_polynomials.txt', i)

print('В файл "Sum_polynomials.txt" записана сумма многочленов следующих файлов: '
      '"Polynomials_file1.txt", "Polynomials_file2.txt"')
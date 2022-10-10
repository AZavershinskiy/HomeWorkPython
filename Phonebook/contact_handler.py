import view


def user_dictionary(check: bool,
                    user_list,
                    new_first_name,
                    new_second_name,
                    new_phone_number,
                    new_note):
    if not (check):
        id = 1
    else:
        id = int(user_list[-1]['id']) + 1
    return [{'id': id, 'Имя': new_first_name,
             'Фамилия': new_second_name,
             'Телефон': new_phone_number,
             'Примечание': '-' if new_note == '' else new_note}]


def find_user(name_reader, user, key, dict_fieldnames):
    user_list = []
    for i in name_reader:
        if user in i[dict_fieldnames[key]]:
            user_list.append(i)
    return user_list


def edit_user(name_reader, user, choice, dict_fieldname):
    if choice[0] == 5:
        choice = []
        for i in dict_fieldname.values():
            choice.append(i)
        for i in name_reader:
            if i['id'] == user:
                for edit_key in choice:
                    i[edit_key] = view.data_request(f'Введите {edit_key}: ')
    else:
        for i in name_reader:
            if i['id'] == user:
                for edit_key in choice:
                    i[dict_fieldname[edit_key]] = view.data_request(
                        f'Введите {dict_fieldname[edit_key]}: ')
    return name_reader


def get_id_user(searched_users, fieldnames):
    if len(searched_users) == 1:
        id_user = searched_users[0]['id']
    elif len(searched_users) > 1:
        print('Необходимо уточнить пользователя')
        view.print_user(searched_users, fieldnames)
        id_user = view.data_request('Укажите id пользователя: ')
    elif len(searched_users) == 0:
        print('Пользователи не найдены')
    return id_user


def delete_user(users, user_id):
    user_ditc = []
    buff_id = 0
    for i in users:
        if i['id'] != user_id:
            user_ditc.append(i)
            buff_id += 1
            user_ditc[buff_id - 1]['id'] = buff_id
    return user_ditc


def data_preparation_user_in_txt(user_list):
    new_user_list = []
    for i in user_list:
        buff_string = ''
        for k in i.values():
            buff_string += f'{k} '
        new_user_list.append(' '.join(buff_string.split()))
    return new_user_list


def data_preparation_user_in_csv(user_list, dict_fieldnames):
    new_user_list = []
    for i in user_list:
        new_dict_user = {}
        user_list = i.split()
        for k in range(1, len(user_list)):
            new_dict_user[dict_fieldnames[k]] = user_list[k]
        new_user_list.append(new_dict_user)
    return new_user_list


def data_preparation_fieldnames_in_txt(fieldnames):
    return ' '.join(fieldnames)
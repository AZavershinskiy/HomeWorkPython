from prettytable import PrettyTable

def data_request(text):
    return input(text)

def print_user(users, fieldnames):
    string = PrettyTable()
    string.field_names = fieldnames
    for i in users:
        result_str = ''
        for k in i.values():
            result_str += f'{k} '   
        string.add_row(list(result_str.split()))
    print(string)
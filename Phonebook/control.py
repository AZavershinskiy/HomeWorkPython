import handler
import view


def controller():
    command = input("""
    Вас приветствует программа
    "ТЕЛЕФОННЫЙ СПРАВОЧНИК"
    
   Команды:
        1 - Показать имеющиеся контакты
        2 - Добавить новый контакт
        3 - Найти контакт

    Введите номер нужной команды: """)
    if command == '1':
        print(view.show_contacts())
    elif command == '2':
        handler.adds_new()
    elif command == '3':


    

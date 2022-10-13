import handler


def controller():
    print("""
    Вас приветствует программа
    "ТЕЛЕФОННЫЙ СПРАВОЧНИК"
        """)
    while True:
        command = input("""     Команды:
            1 - Показать имеющиеся контакты
            2 - Добавить новый контакт
            3 - Редактировать контакт
            4 - Найти контакт
            0 - Выход
        Введите номер нужной команды: """)
        if command == '1':
            handler.show_contacts()
        elif command == '2':
            handler.adds_new()
        elif command == '3':
            handler.editor()
        elif command == '4':
            handler.finder()
        elif command == '0':
            while True:
                prog_exit = input("""
                Завершить программу?
                    1 - ДА
                    2 - НЕТ
             Ответ: """)
                if prog_exit == '1':
                    print('Программа ЗАВЕРШЕНА\n')
                    return
                if prog_exit == '2':
                    print('Завершение ОТМЕНЕНО\n')
                    break
                if prog_exit != '1' or '2':
                    print('Выберите действие!')
                    continue
                
    

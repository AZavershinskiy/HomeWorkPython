# Напишите программу, удаляющую из текста все слова, например, содержащие "абв".


def word_deleter(str1, str2):
    end_str = ' '.join(
        [i for i in list(initial_str.split()) if word_delete not in i])
    return end_str


initial_str = input('Введите предложение из нескольких слов: ')
word_delete = input('Введите слово или часть слова, которое нужно удалить из предложения: ')

print(f'"{word_deleter(initial_str, word_delete)}" <- предложение без удаленного слова')
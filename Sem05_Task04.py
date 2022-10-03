# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

    # Пример:   
    # 'qqqwwwwwrrtyy' -> 'q3w5r2t1y2'
    # 'q3w5r2t1y2' -> 'qqqwwwwwrrtyy'


def compress_string(str_base):
    char = str_base[0]
    count = 1
    result = ''
    for i in range(1, len(str_base)):
        if char == str_base[i]:
            count += 1
        else:
            result += f'{char}{count}'
            char = str_base[i]
            count = 1
    result += f'{char}{count}'
    return result


def data_extraction(compress_string):
    result = ''
    for i in range(0, len(compress_string), 2):
        result += compress_string[i] * int(compress_string[i + 1])
    return result


str_base = 'qqqwwwwwrrtyy'
result_compress = compress_string(str_base)
print(f'Было: "{str_base}", стало: "{result_compress}"')

extraction_str = data_extraction(result_compress)
print(f'Было: "{result_compress}", стало: "{extraction_str}"')
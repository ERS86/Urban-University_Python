def custom_write(file_name, strings):
    string_number = 0
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        string_number += 1
        caret = file.tell()
        file.write(f'{i}\n')
        strings_positions[(string_number, caret)] = i
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

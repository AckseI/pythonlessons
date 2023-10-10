"""
Написать функцию, которая принимает путь к файлу,
текст и номер строки и записывает в файл полученный текст в
указанный номер строки.
"""


def edit_file(base_path, text, line_number):
    with open(base_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        lines.insert(line_number, text + '\n')

        file.seek(0)
        file.writelines(lines)


edit_file('files/txtlab5.txt', "Acksel", 3)

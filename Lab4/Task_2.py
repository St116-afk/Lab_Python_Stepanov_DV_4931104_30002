# TODO импортировать необходимые молули
import json #json
import csv #csv

INPUT_FILENAME = "input.csv"# Указываем имя файла с данными в формате csv, который будем читать
OUTPUT_FILENAME = "output.json"# Указываем имя файла с данными в формате json, в который будем записывать


def task() -> None:# Определяем функцию task, которая не возвращает значения (возвращает None)
    # TODO считать содержимое csv файла
    # Чтение данных из файла CSV
    # Открываем CSV файл в режиме чтения с кодировкой utf-8 для корректного чтения символов
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        # Создаем объект DictReader для построчного чтения CSV-файла в виде словарей,
        # где ключи - это названия столбцов, а значения - данные из этих столбцов
        reader = csv.DictReader(csv_file)
        # Считываем все строки из CSV файла и добавляем их в список data,
        # используя list comprehension (каждая строка хранится как словарь в списке)
        data = [row for row in reader]

    # TODO Сериализовать в файл с отступами равными 4
    # Сериализуем данные в JSON с отступом 4 и записываем в файл
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        # Открываем JSON файл в режиме записи с кодировкой utf-8
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        # Используем функцию json.dump для сериализации (записи) данных из списка data в JSON файл
        # Параметр indent=4 устанавливает отступ в 4 пробела для удобства чтения JSON-файла
        # ensure_ascii=False позволяет сохранить символы в их оригинальной форме (поддержка не-ASCII символов)

if __name__ == '__main__':# Проверка выполнения функции, если скрипт запускается напрямую
    # Нужно для проверки
    task()# Вызываем функцию task, чтобы выполнить чтение из CSV и запись в JSON файл

    with open(OUTPUT_FILENAME) as output_f:# Открываем JSON файл в режиме чтения по умолчанию
        for line in output_f:# Проходим по каждой строке файла циклом for
            print(line, end="")# Печатаем строку из JSON файла

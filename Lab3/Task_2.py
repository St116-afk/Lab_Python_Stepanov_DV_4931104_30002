# TODO Напишите функцию find_common_participants
def find_common_participants(group1,group2,delim=','):#объявляем функцию find_common_participants
    # принимающую две строки, в которых перечислены участники без пробелов,
    # а также необязательный аргумент, отвечающий за разделитель по умолчанию равен запятой.


    # Разделяем строки участников с помощью split(delim)
    # разделяем на множества set() и находим их пересечение с помощью .intersection()
    return sorted(set(group1.split(delim)).intersection(set(group2.split(delim))))

participants_first_group = "Иванов|Петров|Сидоров"#1 строка с участниками
participants_second_group = "Петров|Сидоров|Смирнов"#2 строка с участниками

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group))
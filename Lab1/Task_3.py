list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]# все игроки в общем списке

# индекс середины
middle_index = len(list_players) // 2#находим индекс центрального игрока в списке

first_team = list_players[:middle_index]#записываем список до этого индекса
second_team = list_players[middle_index:]#записываем список после этого индекса

print(first_team)#печатаем 1 команду
print(second_team)#печатаем 2 команду

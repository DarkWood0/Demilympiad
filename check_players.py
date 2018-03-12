from random import shuffle

# Открываются все необходимые для работы файлы (адреса относительные):
# список участников категории, список опубликовавших свои работы, список ссылок на изображения
with open('players_01_raster.txt') as players_text, open('263490_unique/unique_matching.txt') as publishers_text, \
        open('hosting_images_01_raster.txt') as host_img:
    players = players_text.read().split(', ')
    publishers = publishers_text.read().split('\n')
    hosting_images = host_img.read().split(' ')

# Список для хранения участников, прошедших проверку
clear_players = []

# Непосредственно участок проверки
for publisher in publishers:
    splitter = publisher.split(' ', 1)
    try:
        if splitter[1] in players:
            splitter.append(players.index(splitter[1]) + 1)
            clear_players.append(splitter)
    except IndexError:
        continue

# Готовая база данных обработанных данных в виде списка
database = list(zip(clear_players, hosting_images))

# Перемешивание базы данных
shuffle(database)

# Вывод перемешанных данных  
for i in database:
    # Формат вывода:
    # Ник игрока - № в категории - № в перемешанном списке - ссылка на его изображение, загруженное на хостинг
    message = i[0][1] + ' - ' + str(i[0][-1]) + ' - '
    message += str(database.index(i) + 1) + ' - ' + i[1]
    print(message)

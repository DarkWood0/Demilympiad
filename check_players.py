from random import shuffle

with open('players_01_raster.txt') as players_text, open('263490_unique/unique_matching.txt') as publishers_text, open('hosting_images_01_raster.txt') as host_img:
    players = players_text.read().split(', ')
    publishers = publishers_text.read().split('\n')
    hosting_images = host_img.read().split(' ')

clear_players = []

for publisher in publishers:
    splitter = publisher.split(' ',1)
    try:
        if splitter[1] in players:
            splitter.append(players.index(splitter[1])+1)
            clear_players.append(splitter)
    except IndexError:
        continue

database = list(zip(clear_players, hosting_images))

shuffle(database)
  
for i in database:
    #Ник игрока, № в категории, № в перемешанном списке, ссылка на его изображение, загруженное на хостинг
    message = i[0][1] + ' - ' + str(i[0][-1]) + ' - '
    message += str(database.index(i)+1) + ' - ' + i[1]
    print(message)

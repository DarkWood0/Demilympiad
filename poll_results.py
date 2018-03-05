from grab import Grab
from itertools import groupby
import json

g = Grab()

# Список с ссылками на темы голосований (в виде счетчика потому, что они по этапам идут по порядку)
polls_number = ["https://demiart.ru/forum/index.php?&act=ST&f=13&t="+str(i)+"&mode=show&st=" for i in range(263699, 263707)]

# Список занятых мест
all_places = []

# Функция для парсинга тем с голосованиями
def get_data():
	"""Получает результаты голосований"""
    places = g.doc.select("//td[@class='row1 pad-10'][1]")
    for place in places:
        if place.text()[0:2] == "Пр":
            all_places.append("")
        else:
            all_places.append(place.text()[0:-2])

# Собственно, парсинг
for theme in polls_number:
    g.go(theme)
    get_data()

# Разбивка общего списка мест по категориям
places_split = [list(group) for k, group in groupby(all_places, lambda x: x == "") if not k]

# Префикс для абсолютного пути к папке назначения
prefix = 'E:/Illustrator/Contests/demilympiad_2018/'

# Открывается файл протокола, который также разбивается по категориям
with open (prefix + '03_protocol.txt', encoding='utf-8') as protocol_text:
    protocol = protocol_text.read().split('\n')
splitted_protocol = [list(group) for k, group in groupby(protocol, lambda x: x == "") if not k]

# Открывается список игроков
with open(prefix + 'players.json', encoding='utf-8') as players_list:
    players = json.load(players_list)

# Формируется база данных в виде списка
database = list(zip(players, places_split, splitted_protocol))

# Списки очков, соответствующих количеству участников
points_30 = [25,21,18,15,12,10,9,8,7,6,5,4,3,2,1]
points_20 = [15,12,10,8,6,5,4,3,2,1]
points_10 = [10,9,8,7,6,5,4,3,2,1]

# Обработка базы данных
# Если длина списка игроков меньше или равна 10,
# то обрабатывается список points_10
# Если меньше 21 - points_20
# И если меньше или равна 30 - points_30
for data in database:
    if len(data[0]) <= 10:
        for place, points in zip(data[1],points_10):
            try:
                print(data[2][int(place)-1].split(' - ',2)[0] + " - " + str(points))
            except IndexError:
                continue
    elif len(data[0]) < 21:
        for place, points in zip(data[1],points_20):
            try:
                print(data[2][int(place)-1].split(' - ',2)[0] + " - " + str(points))
            except IndexError:
                continue
    elif len(data[0]) <= 30:
        for place, points in zip(data[1],points_30):
            try:
                print(data[2][int(place)-1].split(' - ',2)[0] + " - " + str(points))
            except IndexError:
                continue
	# Между категориями для визуального удобства выводится пустая строка
    print('')
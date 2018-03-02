from grab import Grab
from itertools import groupby
import json

g = Grab()

polls_number = ["https://demiart.ru/forum/index.php?&act=ST&f=13&t="+str(i)+"&mode=show&st=" for i in range(263699, 263707)]

all_places = []

def get_data():
    places = g.doc.select("//td[@class='row1 pad-10'][1]")
    for place in places:
        if place.text()[0:2] == "Пр":
            all_places.append("")
        else:
            all_places.append(place.text()[0:-2])

for theme in polls_number:
    g.go(theme)
    get_data()

places_split = [list(group) for k, group in groupby(all_places, lambda x: x == "") if not k]

prefix = 'E:/Illustrator/Contests/demilympiad_2018/'

with open (prefix + '03_protocol.txt', encoding='utf-8') as protocol_text:
    protocol = protocol_text.read().split('\n')
splitted_protocol = [list(group) for k, group in groupby(protocol, lambda x: x == "") if not k]
##data_from_protocol = [i.split(' - ') for item in splitted_protocol for i in item]

with open(prefix + 'players.json', encoding='utf-8') as players_list:
    players = json.load(players_list)

database = list(zip(players, places_split, splitted_protocol))

points_30 = [25,21,18,15,12,10,9,8,7,6,5,4,3,2,1]
points_20 = [15,12,10,8,6,5,4,3,2,1]
points_10 = [10,9,8,7,6,5,4,3,2,1]

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
    print('')
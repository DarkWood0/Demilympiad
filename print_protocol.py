# Список участников категории из протокола
data_text = """Елена Ту - 13 - 1 - [url=https://ibb.co/gvH1ac][img]https://thumb.ibb.co/gvH1ac/017.jpg[/img][/url]
Mypp - 18 - 2 - [url=https://ibb.co/cRBDMH][img]https://thumb.ibb.co/cRBDMH/04.jpg[/img][/url]
I-Mago - 11 - 3 - [url=https://ibb.co/mH34Tx][img]https://thumb.ibb.co/mH34Tx/03.jpg[/img][/url]
Tappam Wah - 2 - 4 - [url=https://ibb.co/neesgH][img]https://thumb.ibb.co/neesgH/020.jpg[/img][/url]
alliot - 21 - 5 - [url=https://ibb.co/e0KNFc][img]https://thumb.ibb.co/e0KNFc/05.jpg[/img][/url]
Рыжий кАтенок - 4 - 6 - [url=https://ibb.co/cxnpTx][img]https://thumb.ibb.co/cxnpTx/011.jpg[/img][/url]
Елена-1982 - 16 - 7 - [url=https://ibb.co/iu21ac][img]https://thumb.ibb.co/iu21ac/014.jpg[/img][/url]
Delimiterrr - 10 - 8 - [url=https://ibb.co/f7N1ac][img]https://thumb.ibb.co/f7N1ac/012.jpg[/img][/url]
Jul Kiva - 5 - 9 - [url=https://ibb.co/cci7Fc][img]https://thumb.ibb.co/cci7Fc/015.jpg[/img][/url]
Bentanana - 19 - 10 - [url=https://ibb.co/ddmf1H][img]https://thumb.ibb.co/ddmf1H/07.jpg[/img][/url]
Jahmaty - 8 - 11 - [url=https://ibb.co/jU151H][img]https://thumb.ibb.co/jU151H/016.jpg[/img][/url]
Helvende - 9 - 12 - [url=https://ibb.co/eei4Tx][img]https://thumb.ibb.co/eei4Tx/06.jpg[/img][/url]
Пассат - 7 - 13 - [url=https://ibb.co/eVUYMH][img]https://thumb.ibb.co/eVUYMH/09.jpg[/img][/url]
Musyupick - 3 - 14 - [url=https://ibb.co/d9KB8x][img]https://thumb.ibb.co/d9KB8x/02.jpg[/img][/url]
Maler11 - 1 - 15 - [url=https://ibb.co/nkpEvc][img]https://thumb.ibb.co/nkpEvc/018.jpg[/img][/url]
gelveta - 12 - 16 - [url=https://ibb.co/hzFUvc][img]https://thumb.ibb.co/hzFUvc/01.jpg[/img][/url]
denissus - 22 - 17 - [url=https://ibb.co/iKpdox][img]https://thumb.ibb.co/iKpdox/08.jpg[/img][/url]
mendeleeva - 17 - 18 - [url=https://ibb.co/bSr2Fc][img]https://thumb.ibb.co/bSr2Fc/010.jpg[/img][/url]
Tijko - 23 - 19 - [url=https://ibb.co/nFq9Tx][img]https://thumb.ibb.co/nFq9Tx/013.jpg[/img][/url]
Nenz - 20 - 20 - [url=https://ibb.co/jSd4Tx][img]https://thumb.ibb.co/jSd4Tx/00.jpg[/img][/url]
ПтицаСирин - 14 - 21 - [url=https://ibb.co/bDsZvc][img]https://thumb.ibb.co/bDsZvc/019.jpg[/img][/url]"""

# Вывод этого списка в формате "№ в перемешанном списке - ссылка на изображение"
# Проще говоря, просто отбрасывается ник участника и номер в оригинальном списке
data = data_text.split('\n')
for player in data:
  print(player.split(' - ',2)[2])
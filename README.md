# Демилимпиада

[![Demi](https://demiart.ru/forum/uploads20/post-1120952-1515957359-5a5bac6fcad85.png)](https://demiart.ru/forum/index.php?showtopic=263353)

Демилимпиада - крупный конкурс, проходивший с 01.02 по 12.03 2018 года на сайте  [Demiart.ru](https://demiart.ru/forum/index.php). Для облегчения процесса было написано несколько скриптов. Их описание вы и найдете ниже.

*Все скрипты написаны на языке Python 3 (версия 3.6.3)*

### demi_poll

Основной скрипт, скачивающий из указанной темы уникальные для каждого пользователя изображения. Обработанное количество информации сохраняется и при следующем запуска учитываются только новые поступления. Для парсинга используется фреймворк Grab. Непосредственный разбор данных производится при помощи Xpath-выражений.

Обработанная информация записывается в TXT-файл в формате ```полная ссылка на изображение [пробел] ник пользователя```.

### check_players

На основе файла, полученного предыдущим скриптом, и списка игроков (также отдельным файлом) проводится проверка является ли опубликовавший изображение человек участником конкурса.

После этого скрипт берет из еще одного текстового документа ссылки на изображения, соотносит их с участниками и потом случайным образом перемешивает для создания более анонимных и (на мой взгляд) честных голосований.

Этим скриптом формируется окончательный протокол каждой категории конкурса. Использованный формат протокола:

```Ник игрока - № в категории - № в перемешанном списке - ссылка на его изображение, загруженное на хостинг```

### print_protocol

Отбрасывает из протокола ник и номер игрока в категории, чтобы сохранить анонимность голосования. Соответственно, оставляет только номер в перемешанном списке и ссылку на изображение.

### poll_results

Скрипт, парсящий результаты голосований по этапам и выводящий соответствие баллов с занятым местом. Для категорий разной численности соответствует свой список баллов. Таблицу соответствия можно найти на [Google.Docs](https://docs.google.com/spreadsheets/d/1afvrHV94HbiPMk9uYlD90kwnI_w6ByhpVI4R2xwlCtc/edit?usp=sharing).

### categories_template

Дополнительный скрипт, призваный облегчить оформление тем с голосованиями.
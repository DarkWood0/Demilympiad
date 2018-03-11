from grab import Grab
from operator import itemgetter
import os
import json
import urllib.request

g = Grab()

# Ссылка на обрабатываемую тему
url = 'http://demiart.ru/forum/index.php?showtopic=263490'

# Отсекаем от URL темы часть после вопросительного знака
# и добавляем к оставшемуся ссылку на галерею от имени робота форума
login_url = url.split('?')[0] + '?'
gallery_url = login_url + 'act=module&module=gallery&cmd=user&user=2&op=topic_images&topic=' + url.split('=')[1]

g.go(gallery_url)

# Список страниц
pagination = []
# Список пользователей
usernames = []
# Список ссылок на изображения
image_links = []

def get_data():
    """Получает имя пользователя и соответствующую ему ссылку на изображение"""
    # Скрипт выделяет область с именем пользователя и ссылкой на изображение
    user_images = g.doc.select("//div[@class='thumb-cell-pad']")
    # Получает имена пользователей и добавляет в соответствующий список
    for user in user_images:
        selection = user.select("span[@class='thumb_name'][2]").text()
        usernames.append(selection)
    # Здесь получает ссылки на изображения
    for image in user_images:
        selection = image.select(
            "div[@class='wraptocenter']/a/img[@class='shadow']").select(
                '@src').text()
        image_links.append(selection)

# Скрипт проверяет есть ли в данной галерее изображений пагинация (страницы)
pages = g.doc.select("//*[@id='ucpcontent']/table/tr/td/span/a")

# Если страниц больше одной, то формируются ссылки на них,
# которые добавляются в соответствующий список
if pages.exists() == True:
    if len(pages.text()) > 19:
        raise Exception("Слишком много страниц для обработки")
    elif len(pages.text()) > 16:
        kp = pages.text()[-3:]
    elif len(pages.text()) > 15:
        kp = pages.text()[-2:]
    elif len(pages.text()) == 15:
        kp = pages.text()[-1]
    for page in range(0, int(kp)):
        k = 30
        page = page*k
        pagination.append(gallery_url + '&st=' + str(page))
    # Обрабатываются все найденные страницы
    for page in pagination:
        g.go(page)
        get_data()
# Если страница одна, то она не добавляется в список пагинации,
# а сразу обрабатывается
else:
    g.go(gallery_url)
    get_data()

# В этом блоке объявляются переменные для хранения полученных данных
# Во всех ссылках используется принцип "%номер_темы%_%название_папки_и_файла%"
#
unique_images = 'downloaded_images/' + url.split('=')[1] + '_unique/unique_matching.txt'
store_data = 'downloaded_images/data/' + url.split('=')[1] + '_data_state.json'
data_folder = os.path.dirname(store_data)

def ensure_dir(directory):
    """Проверяет существование указанной папки.
Если таковая отсутствует - создает ее."""
    if not os.path.exists(directory):
        os.makedirs(directory)

# Убеждаемся в существовании папки для хранения данных, благодаря которым
# в последующих запусках скрипт будет ориентироваться была ли добавлена
# новая информация в указанную вами тему или нет
ensure_dir(data_folder)


# Проводится проверка длин списков с именами пользователей и изображениями
# Если длины списков различаются скрипт выдаст соответствующую ошибку
if len(usernames) == len(image_links):
    current_state = len(usernames)
else:
    raise Exception('Длина списков различается')

# Создается база данных (в данном случае в виде словаря)
# из имен пользователей и ссылок на изображения
database = dict(zip(usernames[::-1], image_links[::-1]))

def file_directory(filename):
    """Получает имя файла и возвращает из него директорию назначения"""
    directory = os.path.dirname(filename)
    return directory

def clear_dir(directory):
    """Удаляет файлы из указанной директории.
!Важно! Применять после проверки папки на существование
и перед записью в нее новых файлов)"""
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

# Следующая функция сохраняет текущую длину списка пользователей,
# на которую скрипт будет ориентироваться при последующем запуске
def save_data(filename):
    """Сохраняет текущее состояние списка пользователей"""
    with open(filename, 'w') as f_obj:
        json.dump(current_state, f_obj)

# Эта функция сохраняет изображения в папку назначения, при этом задавая порядковый номер по порядку скачивания
# Более старые картинки будут иметь больший номер		
def downloading(data_object, directory):
    """Сохраняет изображения из data_object в directory"""
    for link in data_object:
        image_name = link.rsplit('/',1)[1]
        print('Загружается изображение ' + image_name)
        order_name = str(0) + str(data_object.index(link))
        urllib.request.urlretrieve(link, directory + '/' + order_name + '.' + link.split('.')[2])

def write_to_file(filename, data_object):
    """Записывает соответствие имен пользователей и загруженных ими изображений
в указанный файл. data_object должен быть словарем"""
    for name, link in data_object:
        prepared_links = link + ' ' + name[2:]
        with open(filename, 'a') as output:
            output.write(prepared_links + '\n')

def get_all_matching(usernames, image_links):
    """Получает соответствие всех имен пользователей с загруженными ими
изображениями; передаваемые аргументы должны быть списками"""
    matching = []
    for i in range(max((len(usernames),len(image_links)))):
        while True:
            data = (usernames[i],image_links[i])
            matching.append(data)
            break
    return matching

# По сути основная функция скрипта, в которой применяются созданные выше функции
def print_matching(filename, user_list, image_list, data_object):
    """Скачивает уникальные изображения и распечатывает соответствие их с именами пользователей"""
    directory = file_directory(filename)
    ensure_dir(directory)
    clear_dir(directory)
    downloading(list(data_object.values()), directory)
    write_to_file(filename, data_object.items())

# В этой функции ведется проверка на существование файла, в который записывается количество обработанной информации
# Так как при первом запуске этот файл не существует, то возникнет ошибка,
# которую и перехватывает функция
def check_data_store(data_file=store_data):
    """Проверяет наличие хранилища данных для конкретной темы,
если таковое отсутствует, то создает его"""
    try:
        with open(data_file) as f_obj:
            old_state = json.load(f_obj)
    except FileNotFoundError:
        save_data(data_file)        
        print_matching(unique_images, usernames, image_links, database)
    else:
        return old_state

# Данная функция сверяет равенство старых данных с новыми для конкретной темы
# Если они равны, то выдается сообщение "Нет новых данных", если есть -
# запускается процесс их обработки

# На всякий случай добавлена проверка от уменьшения счетчика новых сообщений
# Если он по какой-то причине станет больше текущего состояния (иными словами,
# текущее состояние будет меньше), то скрипт выдаст соответствующую ошибку
def check_data_state(old_state=check_data_store()):
    """Сверяет равенство старых данных с новыми для конкретной темы"""
    if old_state == current_state:
        print("Нет новых данных")
    elif old_state > current_state:
        raise Exception("счетчик новых сообщений " +
                        "не может иметь отрицательное значение!")
    else:
        user_copy = usernames[:]
        user_copy.clear()
        for user in usernames[old_state:]:
            user_copy.append(user)
        image_copy = image_links[:]
        image_copy.clear()
        for image in image_links[old_state:]:
            image_copy.append(image)
        database_copy = dict(zip(user_copy[::-1], image_copy[::-1]))        
        print_matching(unique_images, user_copy, image_copy, database_copy)
        save_data(store_data)
        
# При первом запуске скрипта перехватывает ошибку, инициируемую
# функцией check_data_state() потому, что необходимый ей для работы
# файл еще не создан. Он будет доступен только при последующих запусках
def first_start():
    try:
        check_data_state()
    except TypeError:
        pass
    
first_start()

# Список категорий в виде текста
categories_text = """растровая графика, векторная графика, живые материалы, фотография, фотоарт, трехмерное 
моделирование, дпи, фрактал-арт """

# Список категорий как переменная
categories = categories_text.split(', ')

# Вывод шаблона для каждой категории
for category in categories:
    if category == 'дпи':
        category = category.upper()
    else:
        category = category.capitalize()
    text = '[c][IMG]http://demiart.ru/forum/uploads20/post-1120952-1515957359-5a5bac6fcad85.png[/IMG]\n'
    text += '[COLOR=orange][SIZE=7]Голосование по второму этапу в категории "' + category + '"[/SIZE][/COLOR]\n'
    text += '[COLOR=yellow][SIZE=7]С 14.02 по 18.02 включительно[/SIZE][/COLOR][/C]\n\n'
    text += 'Выберите три лучших здания.'
    print(text)

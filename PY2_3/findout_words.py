# -*- coding: UTF-8 -*-

import codecs
import json


words = {}
list_of_words = []
list_of_long_words = []


def encoding(file_name):
    if file_name == 'newsfr.json':
        file_encoding = "iso8859_5"
    elif file_name == 'newsit.json':
        file_encoding = "windows-1251"
    elif file_name == 'newscy.json':
        file_encoding = "KOI8-R"
    else:
        file_encoding = "UTF-8"
    return file_encoding


def parsing_file(file_name, word_length, list_words):
    with codecs.open(file_name, encoding=encoding(file_name)) as file_news:

        rss_of_news = json.load(file_news)

        for news in rss_of_news['rss']['channel']['item']:  # Распарсили строку json в список
            try:                                            # Отработка ньюанса в структуре json-файла
                description = news['description']['__cdata']
            except TypeError:
                description = news['description']

            list_words = description.split()                # Добавление в список слов из строки

            for word in list_words:                         # Выборка слов длиннее n количества символов
                if len(word) > word_length:
                    list_of_long_words.append(word)

    for word in list_of_long_words:                         # Подсчет слов, длиннее n количества символов
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    def l(x):
        return x[1]

    list_sorted_words = sorted(words.items(), key=l, reverse=True)

    print('Список первых 10 наиболее часто встречающихся в новостях\
    слов с длиной более {} символов:'.format(word_length))
    for words_selected in list_sorted_words[:10]:  # Печать первых 10 элементов списка
        print(words_selected)


# Панель управления программой

file = input('Укажите с новой строки название файла, который Вы хотите обработать с помощью программы\n')

# file_encoding = input('Укажите с новой строки кодировку файла\n')

word_len = int(input('Укажите с новой строки длинее какого количества символов будут учитываться слова\n'))

parsing_file(file, word_len, list_of_words)

# Информация про кодировки файлов:
# 'newsfr.json' : "iso8859_5"
# 'newsit.json' : "windows-1251"
# 'newscy.json' : "KOI8-R"
# 'newsafr.json' : "UTF-8"

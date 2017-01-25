# -*- coding: UTF-8 -*-

import codecs
import json


words = {}
list_of_words = []
list_of_long_words = []
word_length = 0

def encoding(file_name):
    if file_name == 'newsfr.json':
        file_encoding = "iso8859_5"
    elif file_name == 'newsit.json':
        file_encoding = "windows-1251"
    elif file_name == 'newscy.json':
        file_encoding = "KOI8-R"
    else: file_encoding = "UTF-8"
    return file_encoding

def parsing_file(file_name, word_length):
    with codecs.open(file_name, encoding = encoding(file_name)) as news:

        rss_of_news = json.load(news)

        items = rss_of_news['rss']['channel']['item']         # Распарсили строку json в список
        for item in items:
            for description in item['description'].values():
                list_of_words = description.split()

                for word in list_of_words:              # Выборка слов длиннее n количества символов
                    if len(word) > word_length:
                        list_of_long_words.append(word)

    for word in list_of_long_words:                    # Подсчет слов, длиннее n количества символов
        if word in words:
            words[word] += 1
        else: words[word] = 1

    l = lambda x: x[1]                                  # Формула из http://pytalk.ru/forum/python/24229/
    t3 = sorted(words.items(), key=l, reverse=True)

#    print(sorted(words.items(), key=l, reverse=True))  # Печать полностью всего сортированого списка. Проверка

    for p in t3[:10]:                                   # Печать первых 10 элементов списка
        print(p)

# Панель управления программой

# file_name = input('Укажите с новой строки название файла, который Вы хотите обработать с помощью программы\n')
# file_encoding = input('Укажите с новой строки кодировку файла\n')
# word_length = int(input('Укажите с новой строки длинее какого количества символов будут учитываться слова\n'))

file_name = 'newsfr.json'
#file_encoding = "iso8859_5"
word_length = 6

parsing_file(file_name, word_length)

# Информация про кодировки файлов:
# 'newsfr.json' : "iso8859_5"
# 'newsit.json' : "windows-1251"
# 'newscy.json' : "KOI8-R"
# 'newsafr.json' : "UTF-8"
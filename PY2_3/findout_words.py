# -*- coding: UTF-8 -*-

import codecs
import json


t2 = []
words = {}
with codecs.open('newsfr.json', encoding="iso8859_5") as news:

    get_data = json.load(news)

    y = get_data['rss']['channel']['item']
    for item in y:
        for description in item['description'].values():
            t1 = description.split()
#            print(t1)
            for word in t1:
                if len(word) > 6:
                    t2.append(word)
#                    print(t2)


    for word in t2:                                     # Счет количества слов
        if word in words:
            words[word] += 1
        else: words[word] = 1

    l = lambda x: x[1]                                  # Формула из http://pytalk.ru/forum/python/24229/
    t3 = sorted(words.items(), key=l, reverse=True)
#    print(sorted(words.items(), key=l, reverse=True))  # Печать полностью всего сортированого списка

    for p in t3[:10]:                                   # Печатаем первые 10 элементов списка
        print(p)
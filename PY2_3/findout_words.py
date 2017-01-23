# -*- coding: UTF-8 -*-

import codecs
import json

def parsed_string():
    with codecs.open('newsfr.json', encoding="iso8859_5") as news:
        return json.load(news)

for word in parsed_string():
    if len(word) > 6:
        print(word)


    # for channel in news.values():
    #     for item in channel.values():
    #         for article in item:
    #             print(json.load(article))
import subprocess
import os
import requests


KEY = 'trnsl.1.1.20161216T160124Z.4a07c4b6a2f01566.ade260e6c684818698899fd08a9c15d72faca843'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

# путь к файлу с текстом;
directory_source = 'Source'

# путь к файлу с результатом;
directory_result = 'Result'

# создаем директорию с результатами перевода
create_directory_out = subprocess.run(['mkdir', '-p', './Result'])

# Получаем список файлов в переменную list_files
list_files = os.listdir(directory_source)


# язык с которого перевести;
def choice_language(file, lang_out):
    if file == 'DE.txt':
        lang = 'de-'
    elif file == 'ES.txt':
        lang = 'es-'
    else:
        lang = 'fr-'
    return lang + lang_out


#
def export_mytext(file):
    with open(os.path.join(directory_source, file)) as f:
        text = f.readlines()
        return text


# Функция перевода
def translate_me(mytext, lang):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    params = {
        'key': KEY,
        'text': mytext,
        'lang': lang,
    }
    response = requests.get(URL, params=params)
    return response.json()


second_lang = input('Введите язык, на который следует перевести текст файлов: ')

# Пакетный перевод файлов
for file_name in list_files:
    print(file_name)
    print(choice_language(file_name, second_lang))
    lang_pair = choice_language(file_name, second_lang)
    print(export_mytext(file_name))
    tr = export_mytext(file_name)
    json = translate_me(tr, lang_pair)
    print(' '.join(json['text']))
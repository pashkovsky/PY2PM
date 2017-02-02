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


# чтение текста из файла для перевода
def import_text(file):
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

    Args:
        mytext:
    """
    params = {
        'key': KEY,
        'text': mytext,
        'lang': lang,
    }
    response = requests.get(URL, params=params)
    return response.json()


# запись текста в файл после перевода
def export_text(file, text):
    with open(os.path.join(directory_result, file), 'w') as f:
        f.write(text)
        print('Переведен и сохранен файл ', os.path.join(directory_result, file))


# Пакетный перевод файлов
second_lang = input('Введите язык, на который следует перевести текст файлов, находящихся в папке "Source": ')
for file_name in list_files:
    lang_pair = choice_language(file_name, second_lang) # формируем пару языков для параметров перевода
    text_for_translate = import_text(file_name)         # читаем текст из файла для перевода
    json = translate_me(text_for_translate, lang_pair)  # переведенный текст
    text_after_translate = ' '.join(json['text'])       # форматируем переведенный текст
    export_text(file_name, text_after_translate)        # записываем переведенный текст в файл

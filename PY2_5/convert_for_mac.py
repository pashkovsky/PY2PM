# -*- coding: utf-8 -*-

import subprocess
import os


# Требуемая ширина в пикселях
new_width = '200'

# Создаем директорию, в которую будем помещать конвертированные изображения
create_directory_out = subprocess.run(['mkdir', '-p', './Result'])

# Директория, из которой будем брать изображения
directory_source = 'Source'

# Директория, в которую будем помещать конвертированные изображения
directory_out = 'Result'

# Получаем список файлов в переменную files
files = os.listdir(directory_source)

# Фильтруем список по маске  .jpg в переменную images
# Решение взято с сайтов:
# http://senkler.blogspot.com/2011/04/python.html
# http://tutorialbox.freelancing.lv/tutorials/6
images = filter(lambda x: x.endswith('.jpg'), files)

img_list = list(images)
print(img_list)  # Закомментировать

# if not os.path.isdir(out):
#     os.mkdir(out)

# Отображаем текущую и целевую директории
print('\nТекущая директория – %s' % (os.getcwd()))
print('Директория с обработанными изображениями – %s \n' % directory_out)

# Цикл конвертирования изображений с помощью программы sips
for file_name in img_list:
    print(file_name)  # Закомментировать
    subprocess.run(['sips', '--resampleWidth', 'new_width', '--out', './directory_out/file_name',
                    './directory_source/file_name', ])

# TODO: Разобраться в чем причина ошибки "not a valid file"
# Warning: ./directory_source/file_name not a valid file - skipping Error 4: no file was specified

# Используйте команду sips
# Документация:
# https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/sips.1.html
# Пример использования для нашей задачи:
# sips --resampleWidth 200 myphoto.jpg
# sips --resampleWidth 200 --out ./Result/face-04_200.jpg ./Source/face-04.jpg

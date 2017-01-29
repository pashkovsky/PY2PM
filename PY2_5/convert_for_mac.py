# -*- coding: utf-8 -*-

import subprocess
import os


# Требуемая ширина в пикселях
new_width = '200'

# Директория, из которой будем брать изображения
directory_source = 'Source'

# Директория, в которую будем помещать конвертированные изображения
directory_out = 'Result'

# Создаем директорию, в которую будем помещать конвертированные изображения
os.makedirs(directory_out)

# Получаем список файлов в переменную files
files = os.listdir(directory_source)

# Фильтруем список по маске  .jpg в переменную images
# Решение взято с сайтов:
# http://senkler.blogspot.com/2011/04/python.html
# http://tutorialbox.freelancing.lv/tutorials/6
images = filter(lambda x: x.endswith('.jpg'), files)

img_list = list(images)

# Контроль. Отображаем текущую, целевую директории и список файлов
print('\nТекущая директория – %s' % (os.getcwd()))
print(img_list)
print('Директория с обработанными изображениями – %s \n' % directory_out)

# Цикл конвертирования изображений с помощью команды sips
for file_name in img_list:
    print(file_name)  # Закомментировать
    subprocess.run(['sips', '--resampleWidth', new_width, '--out', os.path.join(directory_out, file_name),
                    os.path.join(directory_source, file_name)])

    # Получил решение проблемы: Warning: ./directory_source/file_name not a valid file - skipping Error 4: no
    # file was specified с помощью обращения:
    # http://stackoverflow.com/questions/41923184/sips-command-in-a-python-script-is-not-working-error-4-no-file-was
    # -specified

    # Документация: https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/sips.1.html

    # Второй способ создания директории
    # create_directory_out = subprocess.run(['mkdir', '-p', './Result'])

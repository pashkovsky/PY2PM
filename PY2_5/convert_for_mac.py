# -*- coding: utf-8 -*-

import subprocess
import os

# Директория, из которой будем брать изображения
directory_source = 'Source'

# Директория, в которую будем помещать конвертированные изображения
directory_out = 'Result'

# Создаем директорию, в которую будем помещать конвертированные изображения
create_directory_out = subprocess.run(['mkdir', '-p', './Result'])
# os.makedirs(directory_out) # Второй способ создания директории,

# Фильтруем список по маске  .jpg в переменную images
# Решение взято с сайтов:
# http://senkler.blogspot.com/2011/04/python.html
# http://tutorialbox.freelancing.lv/tutorials/6
# Получаем список файлов в переменную files
files = os.listdir(directory_source)
images = filter(lambda x: x.endswith('.jpg'), files)

img_list = list(images)


# Цикл конвертирования изображений с помощью команды sips
def convert_images(images_list, width_new_image):
    for file_name in images_list:
        print(file_name)  # Закомментировать
        subprocess.run(['sips', '--resampleWidth', width_new_image, '--out', os.path.join(directory_out, file_name),
                        os.path.join(directory_source, file_name)])


# Контроль. Отображаем текущую, целевую директории и список файлов
print('\nТекущая директория – {0}, в которой находятся папка с иходными {1} и с обработанными файлами {2}' \
      .format((os.getcwd()), directory_source, directory_out))
print('Список изображений, отобранных для конвертации: ', img_list)
# Требуемая ширина в пикселях
new_width = input('Введите ширину сконвертированных изображений, в пискелях: \n')
convert_images(img_list, new_width)

# Получил решение проблемы: Warning: ./directory_source/file_name not a valid file - skipping Error 4: no
# file was specified с помощью обращения:
# http://stackoverflow.com/questions/41923184/sips-command-in-a-python-script-is-not-working-error-4-no-file-was
# -specified

# Документация: https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/sips.1.html

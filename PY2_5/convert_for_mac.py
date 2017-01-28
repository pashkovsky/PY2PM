# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import glob

width = '300'   # Требуемая ширина в пикселях

# extension = ['jpg', 'JPG', 'JPEG','jpeg', 'png', 'gif', 'tiff', 'tif'] # Расширения\Форматы

source = 'Source'
out = 'Result'

files = glob.glob(os.path.join(source, '*.jpg'))

img_list = list(files)
print(img_list)


if not os.path.isdir(out):
    os.mkdir(out)

print('\nТекущая директория %s \n' % (os.getcwd()))
print('\nПапка с обработанными файлами %s \n' % (out))
#
# for elm in list_files:
#     with open(elm) as file:


# Используйте команду sips
#
# Документация:
# https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/sips.1.html
#
# Пример использования для нашей задачи:
# sips --resampleWidth 200 myphoto.jpg
import os
import glob


source = 'Source'

files = glob.glob(os.path.join(source, "*.jpg"))

list_files = list(files)
print(files)

for elm in list_files:
    with open(elm) as file:


# Используйте команду sips
#
# Документация:
# https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/sips.1.html
#
# Пример использования для нашей задачи:
# sips --resampleWidth 200 myphoto.jpg
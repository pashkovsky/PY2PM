
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os


migrations = 'Migrations'

# Запрашиваем строку для поиска
#find_str = input('Введите строку: ')
find_str = 'SELECT'

# Отбираем файлы по маске
files = glob.glob(os.path.join(migrations, "*.sql"))

# Cписок файлов отобранных по маске
files_list =list(files)
print('Начальное количество файлов', len(files_list)) # Убрать

# Контрольный список файлов, которые не содержат строку поиска
files_str_out = []

# Осуществляем поиск в файлах запрошенной строки
for file_name in files_list:
	with open(file_name) as file:
		data = file.read()
		row = data.find(find_str)
		if  row == -1:
			files_str_out.append(file_name)
			files_list.remove(file_name)
			print('Файл {0} удален'.format(file_name)) # Закомментировать. Проверка файлов по списку
		else:
			print('Слова {0} встречаются впервые в файле\
			{1} в строке {2}'.format(find_str, file_name, row))  # Закомментировать. Проверка файлов по списку

print('\nСписок файлов, в которых содержится строка {}:'.format(find_str))
for file_name in files_list:
	print(file_name)
print('Всего: {0} файл(-а)'.format(len(files_list)))

print('\nСписок файлов, в которых НЕ содержится строка {}:'.format(find_str))
for file_name in files_str_out:
	print(file_name)
print('Всего: {0} файл(-а)'.format(len(files_str_out)))
# db_datareader
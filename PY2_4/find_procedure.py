import glob
import os


migrations = 'Migrations'
advanced_migrations = 'Advanced Migrations'

# Отбираем файлы по маске
files = glob.glob(os.path.join(migrations, "*.sql"))
files2 = glob.glob(os.path.join(advanced_migrations, "*.sql"))

# Cписок файлов отобранных по маске
files_list =list(files)
for file in files2:
    files_list.append(file)

print('Количество файлов, которые проверяются в запросе: ', len(files_list))

# Контрольный список файлов, которые не содержат строку поиска
files_str_out = []

# Осуществляем поиск в файлах запрошенной строки
def find_str(files_list, files_str_out, search_line):
    for file_name in files_list:
        with open(file_name) as file:
            try:
                data = file.read()
                row = data.find(search_line)
                if  row == -1:
                    files_str_out.append(file_name)
                    files_list.remove(file_name)
            except:
                print('Обшибка в кодировке файла {0}'.format(file_name))

    return files_list

# Часть кода, если нужна информация на какой строке файла выполняется впервые поисковый запрос
#			print('Файл {0} удален'.format(file_name)) # Закомментировать. Проверка файлов по списку
#		else:
#			print('Слова {0} встречаются впервые в файле\
#			{1} в строке {2}'.format(find_str, file_name, row))  # Закомментировать. Проверка файлов по списку

def files_with_str(files_list):
    print('\nСписок файлов, в которых содержится строка {}:'.format(search_line))
    for file_name in files_list:
        print(file_name)
    print('Всего: {0} файл(-а)'.format(len(files_list)))

def list_files_str_out(files_str_out):
    print('\nСписок файлов, в которых НЕ содержится строка {}:'.format(search_line))
    for file_name in files_str_out:
        print(file_name)
    print('Всего: {0} файл(-а)'.format(len(files_str_out)))

# Панель управления программой:
while files_list is not None:
    print('\nНачинаем поиск')
    search_line = input('Введите условия поиска: ')  # Поисковый запрос
    find_str(files_list, files_str_out, search_line) # Алгоритм стигматизации файлов по условиям поиска
    files_with_str(files_list)                       # Вывод списка файлов, которые  отвечают условиям поиска
#    list_files_str_out(files_str_out)               # Вывод списка файлов, которые НЕ отвечают условиям поиска

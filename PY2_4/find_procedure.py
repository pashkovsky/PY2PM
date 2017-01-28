import glob
import os


migrations = 'Migrations'
advanced_migrations = 'Advanced Migrations'

# Отбираем файлы по маске
files = glob.glob(os.path.join(migrations, "*.sql"))
files2 = glob.glob(os.path.join(advanced_migrations, "*.sql"))

# Cписок файлов отобранных по маске
files_list = list(files)
for file in files2:
    files_list.append(file)

# Контрольный список файлов, которые не содержат строку поиска
files_with_str = []

# Осуществляем поиск в файлах запрошенной строки (алгоритм стигматизации файлов по условиям поиска)
def find_str(files_list, search_line):
    print('Количество файлов, которые проверяются при выполнении поискового запроса: ', len(files_list))
    for file_name in files_list:
        with open(file_name) as file:
            try:
                data = file.read()
                row = data.find(search_line)
                if  row != -1:
                    files_with_str.append(file_name)
            except:
                print('Обшибка в кодировке файла {0}'.format(file_name))

    return files_with_str


def files_with_string(files_with_str):
    print('\nСписок файлов, в которых содержится строка {}:'.format(search_line))
    for file_name in files_with_str:
        print(file_name)
    print('Всего: {0} файл(-а)'.format(len(files_with_str)))


# Панель управления программой:
while files_list is not None:
    print('\nНачинаем поиск')
    search_line = input('Введите условия поиска: ')  # Поисковый запрос
    find_str(files_list, search_line)                # Алгоритм стигматизации файлов по условиям поиска
    files_with_string(files_with_str)                # Вывод списка файлов, которые  отвечают условиям поиска
    files_list = files_with_str[:]                   # Очистка и копирование в files_list элементов результата поиска
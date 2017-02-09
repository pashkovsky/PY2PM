import glob
import os


# директории с файлами для поиска
migrations = 'Migrations'
advanced_migrations = 'Advanced Migrations'


# отбираем файлы по маске
files1 = glob.glob(os.path.join(migrations, "*.sql"))
files2 = glob.glob(os.path.join(advanced_migrations, "*.sql"))


# формируем список файлов, отобранных по маске
def create_files_list(list1, list2):
    result = list(list1)
    for file in list2:
        result.append(file)
    return result


# поиск в строках файлах по условиям поискового запроса
def find_str(list_in, search):
    print('Количество файлов, которые проверяются при выполнении поискового запроса: ', len(list_in))
    found = []
    for file_name in list_in:
        with open(file_name, encoding='utf-8', errors='ignore') as f:
            data = f.read()
            row = data.find(search)
            if row != -1:
                found.append(file_name)
    return found


# вывод списка найденных файлов построчно
# вывод количества найденных файлов
def show_files_with_string(found, search):
    print('\nСписок файлов, в которых содержится строка {}:'.format(search))
    for file_name in found:
        print(file_name)
    print('Всего: {0} файл(-а)'.format(len(found)))


# инкремент итераций ввода поисковых запросов
i = 1


# панель управления программой
while True:
    # ограничиваем использование полного списка файлов для поиска только первой итерацией
    if i == 1:
        files_list = create_files_list(files1, files2)

    # вводим поисковый запрос
    search_line = input('\nНачинаем поиск. \nВведите условия поиска: ')

    # добавляем в список названия файлов, содержащих строки, отвечающие условиям поискового запроса
    files_with_str = find_str(files_list, search_line)

    # выводим список файлов, отвечающих условиям поискового запроса
    show_files_with_string(files_with_str, search_line)

    # очищаем и копируем в files_list элементов результата поиска
    files_list = files_with_str[:]

    i += 1

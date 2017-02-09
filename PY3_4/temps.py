# Входные параметры функции: путь к файлу с данными;
# Семь значений температур по Фаренгейту. Файл temps.txt
# Какая средняя арифм. температура по Цельсию на неделю
# Написать функции, которые на вход примут данные из соответствующих файлов и посчитают результат.
# Результат выводить в консоль.

import osa


PATH = './temps.txt'
URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'


# функция извлечения данных о температуре из файла
def data_extraction(path):
    with open(path) as f:
        result = []
        for row in range(7):
            x = int(f.readline()[0:2])
            result.append(x)
        return result


# функция вычисления среднего арифметического из списка
def calculate_average(lst):
    i = len(lst)
    s = 0
    for elm in lst:
        s = s + elm
    result = s / i
    return result


# функция конвертации температур с помощью ресурса http://www.webservicex.net
def convert_temperature(temperature):
    client = osa.Client(URL)
    response = client.service.ConvertTemp(Temperature = temperature, \
                                          FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')
    return response


# EXECUTE
# отформатированный список температур из файла
data_lst = data_extraction(PATH)

# средняя арифметическая температура по Фарингейту
avg_F = calculate_average(data_lst)

# средняя арифметическая температура по Цельсию
avg_C = convert_temperature(avg_F)
print('%.2f' % avg_C)

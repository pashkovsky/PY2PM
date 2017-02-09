# Входные параметры функции: путь к файлу с данными;
# Семь значений температур по Фаренгейту. Файл temps.txt
#
# Какая средняя арифм. температура по Цельсию на неделю
# Написать функции, которые на вход примут данные из соответствующих файлов и посчитают результат.
# Результат выводить в консоль.
import osa


PATH = './temps.txt'
URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'


def data_extraction(path):
    with open(path) as f:
        result = []
        for row in range(7):
            x = int(f.readline()[0:2])
            result.append(x)
        return result


def calculate_average(lst):
    i = len(lst)
    s = 0
    for elm in lst:
        s = s + elm
    result = s / i
    return result




# EXECUTE
print(data_extraction(PATH))


client = osa.Client(URL)
response = client.service.ConvertTemp(Temperature = '100', FromUnit = 'degreeFahrenheit', ToUnit = 'degreeCelsius')
print(response)








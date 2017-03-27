# Дано: Длина пути в милях, название пути. Файл travel.txt
#(Формат: “<название пути>: <длина в пути> <мера расстояния>”)
# Вопрос: Посчитать суммарное расстояние пути в километрах? Точность: .01 .

from pprint import pprint
import osa


PATH = './travel.txt'
URL = 'http://www.webservicex.net/length.asmx?WSDL'

# функция извлечения количества строк в файле
def calculate_rows(path):
    with open(path) as f:
        result = len(f.readlines())
        return result


# функция извлечения данных о поездках из файла
def data_extraction(path, rows):
    with open(path) as f:
        list_of_travels = []
        for travel in range(rows):
            dict_travels = {}
            travel = list(f.readline().strip().split(' '))

            trace = travel[0][:-1]
            legnth = travel[1].replace(',', '')

            dict_travels['trace'] = trace
            dict_travels['legnth'] = float(legnth)
            list_of_travels.append(dict_travels)
        print(list_of_travels)
        return list_of_travels


# функция перевода миль в км
def convert_distance(distance):
    client = osa.Client(URL)
    response = client.service.ChangeLengthUnit(LengthValue=distance, \
                                          fromLengthUnit='Miles', toLengthUnit='Kilometers')
    print(response)
    return response

# Функция суммирования элементов списка с округлением результата в большее число
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    print(theSum)
    response = round(theSum, 2)
    print(response)
    return response

def info_travel_distance (input_info):
    travels_trace = []
    for line in input_info:
        y = convert_distance(line['legnth'])
        travels_trace.append(y)
    print(travels_trace)
    print('Общее расстояние с учетом всех поездок составляет %0.1f км.' % listsum(travels_trace))


rows = calculate_rows(PATH)
extract = data_extraction(PATH, rows)
info_travel_distance(extract)
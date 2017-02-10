# Дано: Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут и выписывать цены на перелеты.
# Даны цены на билеты в местных валютах. Файл currencies.txt
# (Формат данных в файле: “<откуда куда>: <стоимость билета> <код валюты>”)
# Вопрос: Посчитайте сколько вы потратите на путешествие денег в рублях.
# Точность: без копеек, округлить в большую сторону.

from pprint import pprint
# import osa


PATH = './currencies.txt'
URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'


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
            cost = travel[1]
            code_currency = travel[2]

            dict_travels['trace'] = trace
            dict_travels['cost'] = int(cost)
            dict_travels['code_currency'] = code_currency
            list_of_travels.append(dict_travels)
        return list_of_travels


quantity_rows = calculate_rows(PATH)
data = data_extraction(PATH, quantity_rows)
pprint(data)
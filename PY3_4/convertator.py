import osa

PATH_T = './temps.txt'
PATH_D = './travel.txt'
PATH_C = './currencies.txt'


# функция вычисления среднего арифметического из списка
def calculate_average(list_of_data):
    i = len(list_of_data)
    s = 0
    for elm in list_of_data:
        s = s + elm
    result = s / i
    return result


# функция конвертации температур с помощью ресурса http://www.webservicex.net
def convert_temperature(temperature):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    response = client.service.ConvertTemp(Temperature=temperature, \
                                          FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')
    return response


# функция перевода миль в км
def convert_distance(distance):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    response = client.service.ChangeLengthUnit(LengthValue=distance, \
                                               fromLengthUnit='Miles', toLengthUnit='Kilometers')
    return response


# функция перевода валюты в рубли
def convert_currency(code_currency, sum):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    response = client.service.ConvertToNum(fromCurrency=code_currency, \
                                           toCurrency='RUB', amount=sum, rounding=True)
    return response


# функция извлечения количества строк в файле
def calculate_rows(path):
    with open(path) as f:
        result = len(f.readlines())
        return result


# функция извлечения данных о температуре из файла
def data_extraction_temp(path):
    rows = calculate_rows(path)
    with open(path) as f:
        result = []
        for row in range(rows):
            x = int(f.readline()[0:2])
            result.append(x)
        avg_F = calculate_average(result)
        avg_C = convert_temperature(avg_F)
        return avg_C


# функция извлечения данных о стоимости поездок из файла
def data_extraction_cost(path):
    rows = calculate_rows(path)
    with open(path) as f:
        list_of_cost = []
        for travel in range(rows):
            travel = list(f.readline().strip().split(' '))
            code_currency = travel[2].replace(',', '')
            cost = travel[1].replace(',', '')
            cost_in_RUB = convert_currency(code_currency, cost)
            list_of_cost.append(float(cost_in_RUB))
        sum_cost = round(sum(list_of_cost))
        return sum_cost


# функция извлечения данных о расстояниях поездок из файла
def data_extraction_distance(path):
    rows = calculate_rows(path)
    with open(path) as f:
        list_of_distance = []
        for travel in range(rows):
            travel = list(f.readline().strip().split(' '))
            legnth = travel[1].replace(',', '')
            list_of_distance.append(float(legnth))
        distance_mi = sum(list_of_distance)
        distance_km = convert_distance(distance_mi)
        return distance_km


print('Cредняя арифметическая температура по Цельсию: %.2f' % data_extraction_temp(PATH_T))
print('Сумма расходов на путешествие денег в рублях: %d' % data_extraction_cost(PATH_C))
print('Cуммарное расстояние пути в километрах: %.1f' % data_extraction_distance(PATH_D))

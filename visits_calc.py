# Константы
residence_limit = 90  # 45, 60
schengen_constraint = 180
first_of_january = 1  # первое января текущего года

# Мы тратим в день
cost_per_day = 15

# visits = [[1, 10], [11, 50], [70, 120], [141, 180]]

# Форма для ввода количества поездок в Шенген
visits = []

number_trip = int(input('Ведите количество Ваших поездок в Шенген: '))

print('---------------')

# Форма для ввода дат по каждой из поездок
number_stay = 1
while number_stay <= number_trip:
    print('Данные по поездке № ', number_stay)
    date_in = int(input('Введите дату въезда в Шенген '))
    date_out = int(input('Введите дату выезда из Шенгена '))

    if date_out < date_in:
        print('Неправильно указана дата выезда! \n Повторите ввод всех дат! \
    \n Будьте, пожалуйста, внимательны')
        raise Exception('Дата выезда', date_out, 'раньше даты въезда', date_in)

    visits.append([date_in, date_out])

    print('---------------')

    number_stay += 1


# Проверка введенных дат на ошибки
for visit in visits:

    if not isinstance(visit, list):
        raise Exception("Ошибка в типе поездки", visit)

    # Что будет если дата выезда будет раньше даты въезда? [[1, 10], [19, 2]]
    if visit[0] > visit[1]:
        print('Неправильно указаны даты въезда и выезда!')
        raise Exception("Дата въезда позже даты выезда", visit)


# Общее время в ЕС
days_in_eu = []

# Подсчет количества дней по заездам по нарастающей
total_time_in_eu = 0

for visit in visits:
    past_days = 0
    for past_visit in visits:

        # Что будет если в нашем списке будут накладывающиеся визиты?
        # Где проверочный скрипт указывать подсказал Роман Журавлев (пост в Facebook)
        if past_visit[1] > visit[0] and past_visit[0] < visit[0]:
            print('Неправильно указаны даты въезда и выезда!', past_visit, \
                  visit, past_visit[1], visit[0])
            raise Exception("Вы указали накладывающиеся визиты", past_visit, \
                            visit)

        if past_visit[0] <= visit[0] and past_visit[0] > visit[0] - schengen_constraint:
            past_days += past_visit[1] - past_visit[0] + 1

    days_in_eu.append(past_days)
    total_time_in_eu += visit[1] - visit[0] + 1


# Проверка длительности пребывания в Шенгене
for visit, days in zip(visits, days_in_eu):

    if days > residence_limit:
        print('В течение поездки', visit, 'вы находились в Шенгенском пространстве слишком долго:', days)


if total_time_in_eu > residence_limit:
    print('Вы не можете находиться в Шенгенском пространстве так долго')

print('Вы пробыли в Шенгенском пространстве в ЕС всего:', total_time_in_eu, 'дней')

print('Вы находились в ЕС в пределах последних 180 дней', days, 'дней')

# 2 Планирование визита в будущем по дате въезда.
# Задача: вывести, сколько времени можно пробыть в Шенгене

print('---------------')
print('СЕРВИС ПЛАНИРОВАНИЯ БУДУЩЕЙ ПОЕЗДКИ')
print('---------------')

# Проверяем, желает ли пользователь воспользоваться сервисом
while True:
    user_select = input('Желаете ли Вы расчитать максимальную длительность новой поездки? Укажите: "Да" или "Нет"\n ')
    if user_select == 'Да':

        # Запускаем сервис
        future_trip_in = int(input('Введите дату въезда в Шенген в Вашей планируемой поездке: '))

        # Вводим новую переменную - общее время в ЕС с учетом новой поездки
        future_days_in_eu = []


        for visit in visits:
            past_days = 0
            for past_visit in visits:
                # проверка нет ли наложения даты въезда по новому визиту на старые визиты
                if past_visit[1] > future_trip_in:
                    print('Неправильно указана дата будущего въезда - {0}, пересекающаяся с визитом {1}!'. \
                          format(future_trip_in, past_visit))
                    raise Exception('Вы указали дату въезда в новом визите – {0}, но она накладывается на визит {1}!'. \
                                    format(future_trip_in, past_visit))

                if past_visit[0] <= visit[0] and past_visit[0] > future_trip_in - schengen_constraint:
                    past_days += past_visit[1] - past_visit[0] + 1
            future_days_in_eu.append(past_days)


        # Проверка длительности пребывания в Шенгене
        for visit, days in zip(visits, future_days_in_eu):
            if days > residence_limit:
                print('В течение поездки', visit, 'вы пребывали в ЕС слишком долго:', days)


        future_days_in_eu = 90 - days
        future_date_out_eu = future_trip_in + future_days_in_eu - 1
        if future_days_in_eu >= 0:
            print('Вы находились в ЕС в пределах последних 180 дней перед планируемой поездкой', days, 'дней')
            print('Если Вы въедите в Шенгенское пространство на ', future_trip_in,\
                  'день,', 'то сможете находиться в Шенгенском пространстве ', future_days_in_eu,\
                  'дней – до', future_date_out_eu, 'дня')
        else:
            print('Вы не можете въехать в Шенгенское пространство на ', future_trip_in,\
                  'день, так как превысите допустимое время нахождения в Шенгенском пространстве')

    elif user_select == 'Нет':
        print('Спасибо за то, что воспользовались нашим сервисом! \n Желаем Вам хорошего путешествия!')
        break

# Предположим, что изначальный список визитов: visits = [[1,10], [11,50], [70,120], [141, 180]]
# Если мы будем рассчитывать длительность поездки по планируемой дате заезда и введем 6, то получим:
# Если Вы въедите в Шенгенское пространство на 6 день,
# то сможете находиться в Шенгенском пространстве -51 дней – до -46 дня
# Согласитесь, достаточно контринтуитивное поведение программы.
# Пользователю вообще лучше не показывать заведомо неверные числа (отрицательные).
# Нужно как-то иначе обрабатывать такие проблемы. Либо вообще запретить ввод будущих дат заезда меньше,
# чем последний день фактического выезда, либо выводить корректные сообщения с ошибками/правильным расчетом.
# То же самое с вводом будущей даты заезда, если на эту дату еще будет действовать ограничение.
# Т.е. если мы с тем же списком визитов введем 181, то получим: Если Вы въедите в Шенгенское пространство на 181 день,
# то сможете находиться в Шенгенском пространстве -41 дней – до 139 дня Зачем данная информация пользователю?
# Лучше просто сообщить, что въехать невозможно, т.к. нарушается ограничение.


# 1
# Что будет если в нашем списке будут накладывающиеся визиты? [[1, 10], [5, 15]]
# Что будет если дата выезда будет раньше даты въезда? [[1, 10], [19, 2]]
# Такой ситуации допустить нельзя!
# Прекратите выполнение программы в этом случае.
# Чтобы прекратить выполнение программы воспользуйтесь конструкцией: raise Exception(«Ошибка!")
# Прочитайте про raise

# 2
# Я планирую ещё один визит в будущем.
# Я знаю дату въезда.
# Вывести, сколько времени я смогу пробыть в Шенгене

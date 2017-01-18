# Генеральная задача - сформировать словарь в рез-те
# чтения списка рецептов из файла cook_book.txt
# Стр-ра построчная:
# 1 - название блюда, 2 - кол-во ингредиентов
# 3 и далее - ингредиенты (name | quantity | measure)
# Сгенерировать список

cook_book = {}
dish = {}

with open('cook_book.txt') as book:

    for line in book:
        if not line.isspace():
            dish_name = line.strip()
            quantity_ingridients = int(book.readline())
            dish['name'] = dish_name
            dish['type'] = '2'
    #        print(dish)

            list_of_ingridients = []

            for ingridient in range(quantity_ingridients):

                dict_ingridients = {}
                ingridient = list(book.readline().strip().split('|'))
    #            print('характеристика ингридиента', ingridient)
                product = ingridient[0]
                quantity = ingridient[1]
                unit = ingridient[2]

                dict_ingridients['unit'] = unit
                dict_ingridients['quantity'] = quantity
                dict_ingridients['product'] = product
                list_of_ingridients.append(dict_ingridients)
    #            print(ingridient)
    #            print(dict_ingridients)
    #            print('List of ingridients', list_of_ingridients)
            dish['ingridients'] = list_of_ingridients
            cook_book[dish_name] = dish
    print(cook_book)

#        print (line.strip())

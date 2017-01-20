#Можно ли собрать библиотеку из рецептов по разделам:
# закуски, 2-е, десерты.
# Потом создать функцию которая будет выводить список и количество продуктов при
# выборе 1,2,3 блюда на _____ персон. В итоге вывести на печать список покупок.

cook_book = {}

# Функция чтения данных о меню с файла
def create_dict_dishs(file_name):
    with open(file_name) as book:

        for line in book:
            if not line.isspace():
                dish = {}
                dish_name = line.strip()
                quantity_ingridients = int(book.readline())
                dish['name'] = dish_name
                dish['type'] = '2'

                list_of_ingridients = []

                for ingridient in range(quantity_ingridients):

                    dict_ingridients = {}
                    ingridient = list(book.readline().strip().split('|'))

                    product = ingridient[0]
                    quantity = ingridient[1]
                    unit = ingridient[2]

                    dict_ingridients['unit'] = unit
                    dict_ingridients['quantity'] = int(quantity)
                    dict_ingridients['product'] = product
                    list_of_ingridients.append(dict_ingridients)
                dish['ingridients'] = list_of_ingridients
                cook_book[dish_name] = dish
        return cook_book

def get_shop_list_by_dishes(dishes, people_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in dish['ingridients']:
            new_shop_item = dict(ingridient)
            # пересчитали ингредиенты по количеству людей
            new_shop_item['quantity'] = new_shop_item['quantity'] * people_count
            if new_shop_item['product'] not in shop_list:
                shop_list[new_shop_item['product']] = new_shop_item
            else:
                shop_list[new_shop_item['product']]['quantity'] += new_shop_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for key, shop_list_item in shop_list.items():
        print("{product} {quantity} {unit}".format(**shop_list_item))

def create_shop_list(people_count, first_dish, second_dish, third_dish):
    # получить блюда из кулинарной книги
    dish1 = cook_book[first_dish]
    dish2 = cook_book[second_dish]
    dish3 = cook_book[third_dish]
    dishes = [dish1, dish2, dish3]
    #заполнили список покупок
    shop_list = get_shop_list_by_dishes(dishes, people_count)
    # Вывести список покупок
    print_shop_list(shop_list)

def list_of_dishes(people_count, first_dish, second_dish, third_dish):
    print('Вами выбраны для приготовления следующие блюда: {0}, {1}, {2} для {3} чел.'.format(first_dish.lower(), second_dish.lower(), third_dish.lower(), people_count))

# По умолчанию, для тестирования имя файла,
# находящегося в той же директории, что и файл shop_list.py,
# cook_book.txt
file_name = input('Укажите название файла с меню (с расширением *.txt (для эксперимента можете указать cook_book.txt))\n')
create_dict_dishs(file_name)
print('Выберите первое блюдо: ')
first_dish = input()
print('Выберите второе блюдо: ')
second_dish = input()
print('Выберите третье блюдо: ')
third_dish = input()
print('На сколько человек?')
people_count = int(input())
print('***')
list_of_dishes(people_count, first_dish, second_dish, third_dish)
print('\nСписок покупок: ')
create_shop_list(people_count, first_dish, second_dish, third_dish)

# Генеральная задача - сформировать словарь в рез-те
# чтения списка рецептов из файла cook_book.txt
# Стр-ра построчная:
# 1 - название блюда, 2 - кол-во ингредиентов
# 3 и далее - ингредиенты (name | quantity | measure)


with open('cook_book.txt') as book:
    for line in book:
        type(line)
        dish_name = line.strip()
        quantity_ingredients = int(book.readline())
        print(dish_name, quantity_ingredients)
        for ingridient in range(quantity_ingredients + 1):
            ingridient = book.readline().strip()
            print(ingridient)

#        print (line.strip())

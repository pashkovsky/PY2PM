#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from pprint import pprint

cook_book = {}

with open('cook_book.txt') as book:
    for line in book:
        if not line.isspace():
            dish = {}
            dish_name = line.strip()
            quantity_ingridients = int(book.readline())
            dish['name'] = dish_name
            dish['quantity_ingridients'] = quantity_ingridients

            list_of_ingridients = []

            for ingridient in range(quantity_ingridients):
                dict_ingridients = {}
                ingridient = list(book.readline().strip().split('|'))

                product = ingridient[0]
                quantity = ingridient[1]
                unit = ingridient[2]

                dict_ingridients['unit'] = unit
                dict_ingridients['quantity'] = quantity
                dict_ingridients['product'] = product
                list_of_ingridients.append(dict_ingridients)

            dish['ingridients'] = list_of_ingridients
            cook_book[dish_name] = dish
    print(cook_book)

with open('cook_book_auto.json', mode='w') as f:
    json.dump(cook_book, f)

with open('cook_book_auto.json') as readfile:
    looking = json.load(readfile)
    pprint(looking)
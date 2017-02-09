# -*- coding: UTF-8 -*-

from pprint import pprint
import requests


APP_ID = 5866666
USER_ID = 8671131
VERSION = 5.62


# функция импорта списка друзей
def create_friends_list(user_id):
    params = {
        'user_id': user_id,
        'order': 'name',
        'v': VERSION,
        'count': '20'
        #'fields': 'domains'
    }

    response = requests.get('https://api.vk.com/method/friends.get', params)
    result = response.json()
    friend_id_list = []
    if result.get('error') is None:
        for friend_id in result['response']['items']:
            friend_id_list.append(friend_id)
        return friend_id_list


# Функция импорта персональных данных
def import_users_data(user_ids_list):
    user_ids_list = str(user_ids_list)
    params = {
        'user_ids': user_ids_list,
        'v': VERSION,
        'order': 'name',
        'fields': 'last_name, first_name'
    }

    response = requests.get('https://api.vk.com/method/users.get', params)
    if response.json().get('error') is None:
        result = response.json()['response']
        return result

# Функция создания пар друг : друг друга для реализации анализа пересечения
def create_pairs_friends(dict_friends):
    pairs_friends_list = []
    for key in dict_friends:
        if dict_friends[key] is not None:
            for friend_friend in dict_friends[key]:
                pairs_friends_list.append([key, friend_friend])
    return pairs_friends_list


# Получите список всех своих друзей;
my_friends_list = create_friends_list(USER_ID)
print('Список моих друзей, ФИО: ')
pprint(import_users_data(my_friends_list))


# Для каждого своего друга получите список его друзей;
dict_friends = {}
for friend in my_friends_list:
    friends_friends_list = create_friends_list(friend)
    print('Список друзей {0} {1}: \n{2}'.format(import_users_data(friend)[0]['last_name'], \
                                              import_users_data(friend)[0]['first_name'], \
                                              import_users_data(friends_friends_list)))
    print('-------------------------------')
    dict_friends[friend] = friends_friends_list


#
# new_friends_list = [['Коля', 97990388], ['Коля', 13842212], ['Серега', 285504492], ['Серега', 97990388],
#                     ['Макс', 4602111], ['Макс', 97990388], ['Егор', 285504492], ['Егор', 97990388]]

def create_mutual_friends_dict(dict_friends):
    new_friends_list = create_pairs_friends(dict_friends)
    mutual_friends_dict = {}
    for friend in new_friends_list:
        temporary_list = new_friends_list[1:]
        a = friend[1]

        if mutual_friends_dict.get(a) is None:
            mutual_friends_set = set()
            mutual_friends_dict[a] = mutual_friends_set

        for friend_friend in temporary_list:
            if friend[1] == friend_friend[1]:
                b = friend[0]
                c = friend_friend[0]

                if b or c not in mutual_friends_set:
                    mutual_friends_set.add(b)
                    mutual_friends_set.add(c)
                temporary_list.remove(friend_friend)

        new_friends_list = temporary_list

        if mutual_friends_dict[a] == set():
            mutual_friends_dict.pop(a)
        return mutual_friends_dict

print('пересечения (общих друзей) между всеми пользователями: ', create_mutual_friends_dict(dict_friends))

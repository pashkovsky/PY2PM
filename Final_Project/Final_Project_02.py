#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
# from urllib.parse import urlencode, urlparse

import requests

import operator

import json


# Получает Id знаменитости ВКонтакте
# USER_ID = int('Введите ниже id пользователя вКонтакте: \n')

AUTORIZE_URL = 'https://oauth.vk.com/authorize'
APP_ID = 5977252
USER_ID = 80491907  # закомментировать
VERSION = 5.62

dict_groups_title = {}

access_token = '335bb3fd921064dcd79200be48140c27bccaba002e60a94709292043aabc0aa28fe7df3929e1968310e5e'


def count_followers(user_id):
    params = {
        'access_token': access_token,
        'user_id': user_id,
        'v': 5.63,
        'fields': 'count'
    }
    out = requests.get('https://api.vk.com/method/users.getFollowers', params)
    result = out.json()
#    print(result)
    count_followers = result['response']['count']
    return count_followers


# Находит всех подписчиков знаменитости
def create_followers_list(user_id):
    followers_id_list = []

    params = {
        'access_token': access_token,
        'user_id': user_id,
        'v': 5.63,
        'count': '1000',
    }
    response = requests.get('https://api.vk.com/method/users.getFollowers', params)
    result = response.json()
    if result.get('error') is None:
        for follower_id in result['response']['items']:
            if follower_id not in followers_id_list:
                followers_id_list.append(follower_id)
    print('Count followers import to list: ', len(followers_id_list))
    return followers_id_list

# Находит всех друзей знаменитости
def create_friends_list(user_id):
    params = {
        'user_id': user_id,
        'order': 'name',
        'v': VERSION,
        'count': '1000'
    }

    response = requests.get('https://api.vk.com/method/friends.get', params)
    result = response.json()
    friend_id_list = []
    if result.get('error') is None:
        for friend_id in result['response']['items']:
            friend_id_list.append(friend_id)
        return friend_id_list


# создание общего списка пользователей из числа подписчиков и друзей известности
def create_common_list(list1,list2):
    response = list1 + list2
    return response


# функция извлечения данных о группе и создания пар группа : юзер
def import_id_groups_per_users(user_id, list):
    params = {
        'user_id': user_id,
        'access_token': access_token,
        'v': 5.63,
        'extended': 1
    }

    response = requests.get('https://api.vk.com/method/groups.get', params)
    result = response.json()
    try:
        if result['response']['count'] > 0:
            result = result['response']['items']

            for group in result:
                group_title = group['name']
                group_id = group['id']
                list.append([group_id, user_id])

                if group_id not in dict_groups_title:
                    dict_groups_title[group_id] = group_title
    except:
        pass
    return list


# формирование общего списка пар группа : юзер
def create_common_list_pairs_group_and_users(list):
    common_list = []
    count_user = 0
    for user in list:
        import_id_groups_per_users(user, common_list)
        count_user += 1
        print('User: ', count_user)
    return common_list


# создание словаря групп с пользователями (група: [пользователь 1, пользователь 2...]
def invert_list_to_dict(list):
    dict_groups = {}
    for el in list:
        a = el[0]
        b = el[1]
        if a not in dict_groups.keys():
            dict_groups[a] = [b]
        else:
            dict_groups[a].append(b)
    return dict_groups


# присвоение количества участников группы из числа подписчиков знаменитости
def set_count_users_group(dict_in):
    dict_with_count = {}
    for i in dict_in:
        dict_with_count[i] = len(dict_in.get(i))
    return dict_with_count


# 4) Показывает топ 100 групп по количеству подписчиков знаменитости
def slice_top_100(dict):
    dc_sort = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    top100 = dc_sort[:100]
    pprint(top100)
    response = {}
    for i in top100:
        dict_temp = {}
        key = i[0]
        dict_temp[key] = i[1]
        response.update(dict_temp)
    return response


# Присвоение имени группы
def set_title(id):
    if id in dict_groups_title:
        response = dict_groups_title[id]
    return response


# Добавляем ключи title, id и count
def added_new_keys(dict):
    response = []
    for i in dict:
        dict_group = {}
        dict_group['id'] = i
        dict_group['count'] = dict.get(i)
        dict_group['title'] = set_title(i)
        response.append(dict_group)
    return response


# Топ 100 групп должны сохранятся в файл в формате json в формате:
# [
# {‘title’: ‘Название группы’, ‘count’: число_подписчиков},
# {‘title’: ‘Название группы2’, ‘count’: число_подписчиков_2}, ... ]

def write_to_json(dict):
    with open('top100groups80491907_1070.json', mode='w', encoding="utf-8") as f:
        json.dump(dict, f, ensure_ascii=False)
        f.close()


count_folls = count_followers(USER_ID)
print(count_folls)

followers = create_followers_list(USER_ID)
print('КОЛИЧЕСТВО ФОЛЛОВЕРОВ', len(followers))

friends = create_friends_list(USER_ID)
print('КОЛИЧЕСТВО ФРЕНДОВ: ', len(friends))

common_list = create_common_list(followers, friends)
print('КОЛИЧЕСТВО ЮЗЕРОВ: ', len(common_list))
with open('list_folls02.json', mode='w', encoding="utf-8") as f:
    json.dump(common_list, f, ensure_ascii=False)
    f.close()

list_pairs = create_common_list_pairs_group_and_users(common_list)

dict_groups = invert_list_to_dict(list_pairs)

dict_with_count = set_count_users_group(dict_groups)

top100 = slice_top_100(dict_with_count)

result = added_new_keys(top100)
pprint(result)

print('Количество групп: ', len(result))

write_to_json(result)

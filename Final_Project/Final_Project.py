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
APP_ID = 5972820
USER_ID = 621819  # закомментировать
VERSION = 5.62

dict_groups_title = {}

access_token = '3bcd2395276126d86b30b2564b4ee8f806230fb9822a823a1f318dae458b6140ebf02ff8041a336759eab'


def count_followers(user_id):
    params = {
        'access_token': access_token,
        'user_id': user_id,
        'v': 5.63,
        'fields': 'count'
    }
    out = requests.get('https://api.vk.com/method/users.getFollowers', params)
    result = out.json()
    count_followers = result['response']['count']
    return count_followers


# Находит всех друзей и подписчиков знаменитости
def create_followers_list(user_id):
    params = {
        'access_token': access_token,
        'user_id': user_id,
        'v': 5.63,
        'count': '30',
    }
    response = requests.get('https://api.vk.com/method/users.getFollowers', params)
    result = response.json()
#    print(result)
    followers_id_list = []
    if result.get('error') is None:
        for follower_id in result['response']['items']:
            followers_id_list.append(follower_id)
        return followers_id_list


# функция импорта списка друзей
def create_friends_list(user_id):
    params = {
        'user_id': user_id,
        'order': 'name',
        'v': VERSION,
        'count': '30'
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
#    print('RESULT1', result)
    try:
        if result['response']['count'] > 0:
            result = result['response']['items']
#            print('RESULT2',result)
            for group in result:
#                print('GROUP', group)
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
    print(len(list))
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


# присвоение имени группы по ее id
def set_title_group(dict_id, dict_name):
    dict_with_title = {}
    for i in dict_id:
        for x in dict_name:
            if i == x:
                y = dict_name[x]
                z = dict_id[i]
                dict_with_title[y] = len(z)
    return dict_with_title

# 4) Показывает топ 100 групп по количеству подписчиков знаменитости
def slice_top_100(dict):
    dc_sort = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    top100 = dc_sort[:100]
    response = {}
    for i in top100:
        dict_temp = {}
        key = i[0]
        dict_temp[key] = i[1]
        response.update(dict_temp)
    return response

# Добавляем ключи title и count
def added_new_keys(dict):
    response = []
    for i in dict:
        dict_pair = {}
        dict_pair['title'] = i
        dict_pair['count'] = dict.get(i)
        response.append(dict_pair)
    return response


# Топ 100 групп должны сохранятся в файл в формате json в формате:
# [
# {‘title’: ‘Название группы’, ‘count’: число_подписчиков},
# {‘title’: ‘Название группы2’, ‘count’: число_подписчиков_2}, ... ]

def write_to_json(dict):
    with open('top100groups.json', mode='w', encoding="utf-8") as f:
        json.dump(dict, f)
        f.close()


followers = create_followers_list(USER_ID)
friends = create_friends_list(USER_ID)
common_list = create_common_list(followers, friends)
# print('COMMON LIST: ', common_list)
list_pairs = create_common_list_pairs_group_and_users(common_list)
#print(list_pairs)
dict_groups = invert_list_to_dict(list_pairs)
dict_groups = set_title_group(dict_groups, dict_groups_title)
dict_top100 = slice_top_100(dict_groups)
result = added_new_keys(dict_top100)
print('Количество групп: ', len(dict_top100))
pprint(result)

write_to_json(result)

# -*- coding: UTF-8 -*-

# from pprint import pprint

import requests


USER_ID = 8671131
VERSION = 5.62


# функция импорта списка друзей
def friends_list(user_id):
    params = {
        'user_id': user_id,
        'order': 'name',
        'v': VERSION,
        'count': '3',
        'fields': 'domains'
    }

    response = requests.get('https://api.vk.com/method/friends.get', params)
    result = response.json()
    if result.get('error') is None:
        return result['response']['items']



# Получите список всех своих друзей;
my_friends_list = friends_list(USER_ID)
print('Список моих друзей: ', my_friends_list)

# Для каждого своего друга получите список его друзей;
for friend in my_friends_list:
    my_friend_name = '{0} {1}'.format(friend['last_name'], friend['first_name'])
    my_friend_id = friend['id']
    fiends_friends_list = friends_list(my_friend_id)
    print('Список друзей {0}: {1}'.format(my_friend_name, fiends_friends_list))


# найти пересечения (общих друзей) между всеми пользователями

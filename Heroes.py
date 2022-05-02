import requests


def get_heroes(heroes_list):
    heroes = {}
    token = '2619421814940190'
    url = 'https://superheroapi.com/api/' + token + '/search/'
    for hero in heroes_list:
        work = requests.get(url + hero).json()
        for info in work['results']:
            if info['name'] == hero:
                heroes[hero] = int(info['powerstats']['intelligence'])
    return max(heroes, key=heroes.get)


print(get_heroes(['Hulk', 'Captain America', 'Thanos']))

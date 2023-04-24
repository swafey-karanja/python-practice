anime = {}

anime ['naruto'] = {
    'MC' : 'uzumaki naruto',
    'setting' : 'Konoha',
    'antagonist' : 'uchiha madara',
    'favourite character' : 'namikaze minato',
    'rating' : '8/10'
}
anime ['Jujutsu kaisen'] = {
    'MC' : 'itadori yuji',
    'setting' : 'tokyo',
    'antagonist' : 'ryomen sukuna',
    'favourite character' : 'gojo satoru',
    'rating' : '8/10'
}

anime ['attack on titan'] = {
    'MC' : 'eren jeager',
    'setting' : 'paradis',
    'antagonist' : 'zeke jeager',
    'favourite character' : 'levi ackerman',
    'rating' : '9/10'
}

anime ['FMAB'] = {
    'MC' : 'Edward elric',
    'setting' : 'amestris',
    'antagonist' : 'father',
    'favourite character' : 'envy',
    'rating' : '9/10'
}

anime ['hells paradise'] = {
    'MC' : 'gabimaru',
    'setting' : 'paradise',
    'antagonist' : 'unknown',
    'favourite character' : 'gabimaru the hollow',
    'rating' : '7/10'
}

import json
s = json.dumps(anime)
with open("C://Users//Swafey//PycharmProjects//pythonProject1//dictionary//anime.txt","w") as a:
    a.write(s)

def read():
    a = open("C://Users//Swafey//PycharmProjects//pythonProject1//dictionary//anime.txt", "r")
    baah = a.read()
    print(baah)
    anime2 = json.loads(baah)
    print(anime2)
    print(type(anime2))


def print_MC():
    print(anime['FMAB']['MC'])
    print(anime['naruto']['MC'])
    print(anime['Jujutsu kaisen']['MC'])
    print(anime['attack on titan']['MC'])
    print(anime['hells paradise']['MC'])

def print_rating():
    print(anime['FMAB']['rating'])
    print(anime['naruto']['rating'])
    print(anime['Jujutsu kaisen']['rating'])
    print(anime['attack on titan']['rating'])
    print(anime['hells paradise']['rating'])

read()
print_MC()
print_rating()
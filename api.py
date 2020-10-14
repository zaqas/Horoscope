import requests

def Signs():
    response = requests.get('http://sandipbgt.com/theastrologer/api/sunsigns').json()
    for item in response:
        print(f'- {item.title()}')

def Horoscope(user_input,time):
    if time == 'today':
        today = requests.get(f'http://sandipbgt.com/theastrologer/api/horoscope/{user_input}/today').json()
        print(today['horoscope'])
    elif time =='yesterday':
        yesterday = requests.get(f'http://sandipbgt.com/theastrologer/api/horoscope/{user_input}/yesterday').json()
        print(yesterday['horoscope'])
    elif time =='tomorrow':
        tomorrow = requests.get(f'http://sandipbgt.com/theastrologer/api/horoscope/{user_input}/tomorrow').json()
        print(tomorrow['horoscope'])
    else:
        print('Please check your input.')
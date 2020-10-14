# Daily Horoscope

import api

print('List of signs: ')
api.Signs()

user_input = input('What is your sign?\n').lower()

time = input('"yesterday" "today" or "tomorrow"?\n').lower()

api.Horoscope(user_input,time)

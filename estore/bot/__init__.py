from typing import Tuple, List

API_TOKEN: str = '550173812:AAG9eR9G-jLvfKAgTGzZMAPL4IdlAb1jjWc'
COMMANDS: Tuple[str, ...] = ('start', 'help')
WELCOME_MESSAGE: str = "Hey! I'm a bot of an Estore, how can i help you?"
ERROR_MESSAGE: str = "Sorry I can't figure our your request, please use buttons below!"
DELIVERY_METHODS: str = 'Delivery methods'
DELIVERY_REPLY: str = 'Here are next delivery methods'
PAYMENT_METHODS: str = 'Payment methods'
PAYMENT_REPLY: str = 'Here are next payment methods'
LOCATION: List[str] = ['location']
NEAREST_STORE: str = 'Here is a nearest store according to your location'

STORES: Tuple[dict, ...] = (
    {'title': 'London Estore',
     'lons': '0.156853',
     'lats': '51.520812',
     'address': '34 Baker Street, Oatley, NSW 2223'},

    {'title': 'Toronto Estore',
     'lons': '79.345748',
     'lats': '43.704126',
     'address': '27 N Grandstand N Ramp'},

    {'title': 'Kyiv Estore',
     'lons': '30.553835',
     'lats': '50.436446',
     'address': 'Ivana Mazepy St, 17'},
)
from typing import Tuple, List
from telebot import TeleBot

_API_TOKEN: str = '550173812:AAG9eR9G-jLvfKAgTGzZMAPL4IdlAb1jjWc'

COMMANDS: Tuple[str, ...] = ('start', 'help')
WELCOME_MESSAGE: str = "Hey! I'm a bot of an Estore, how can i help you?"
DELIVERY_METHODS: str = 'Delivery methods'
DELIVERY_REPLY: str = 'Courier delivery, USA Post Office'
PAYMENT_METHODS: str = 'Payment methods'
PAYMENT_REPLY: str = 'Cash, bank transaction'
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

BOT: TeleBot = TeleBot(_API_TOKEN)

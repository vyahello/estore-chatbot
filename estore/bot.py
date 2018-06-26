from geopy.distance import vincenty
from telebot import TeleBot
from telebot.types import Message
from estore.keyboard import MarkUpMenu, Menu
from estore import COMMANDS, WELCOME_MESSAGE, DELIVERY_METHODS, DELIVERY_REPLY, PAYMENT_METHODS, \
    PAYMENT_REPLY, LOCATION, NEAREST_STORE, STORES, BOT

bot: TeleBot = BOT
markup_menu: Menu = MarkUpMenu()


@bot.message_handler(commands=COMMANDS)
def send_message(message: Message):
    bot.reply_to(message, WELCOME_MESSAGE, reply_markup=markup_menu.reply())


@bot.message_handler(func=lambda message: True)
def reply_all(message: Message):
    if message.text == DELIVERY_METHODS:
        bot.reply_to(message, DELIVERY_REPLY, reply_markup=markup_menu.reply())
    elif message.text == PAYMENT_METHODS:
        bot.reply_to(message, PAYMENT_REPLY, reply_markup=markup_menu.reply())
    else:
        bot.reply_to(message, message.text, reply_markup=markup_menu.reply())


@bot.message_handler(func=lambda message: True, content_types=LOCATION)
def stores_location(message: Message):
    lon: float = message.location.longitude
    lat: float = message.location.latitude

    distance = []
    for loc in STORES:
        result: vincenty = vincenty((loc['lats'], loc['lons']), (lat, lon))
        distance.append(result)
    index = distance.index(min(distance))
    bot.send_message(message.chat.id, NEAREST_STORE)
    bot.send_venue(message.chat.id,
                   STORES[index]['lats'],
                   STORES[index]['lons'],
                   STORES[index]['title'],
                   STORES[index]['address'])

from typing import List
from geopy.distance import vincenty
from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from estore.bot import API_TOKEN, COMMANDS, MESSAGE, LOCATION, STORES
from estore.options.keyboards import BotKeyboard
from estore.options.menu import Menu, MarkUpKeyboardMenu

bot: TeleBot = TeleBot(API_TOKEN)
menu: Menu = MarkUpKeyboardMenu(BotKeyboard(resize_keyboard=True, row_width=1))


@bot.message_handler(commands=COMMANDS)
def send_message(message: Message) -> None:
    bot.reply_to(message, MESSAGE['welcome'], reply_markup=menu.requests())


@bot.message_handler(func=lambda message: True)
def reply_all(message: Message) -> None:
    reply = menu.replies()
    if message.text == MESSAGE['delivery']['methods']:
        bot.reply_to(message, MESSAGE['delivery']['reply'], reply_markup=reply.delivery())
    elif message.text == MESSAGE['payment']['methods']:
        bot.reply_to(message, MESSAGE['payment']['reply'], reply_markup=reply.payment())
    else:
        bot.reply_to(message, MESSAGE['error'])


@bot.callback_query_handler(func=lambda call: True)
def call_back(call: CallbackQuery) -> None:
    method: str = 'payment' if call.data is ('cash' or 'card' or 'invoice') else 'delivery'
    reply = menu.replies().payment() if method is 'payment' else menu.replies().delivery()
    bot.send_message(call.message.chat.id,
                     text=MESSAGE[method]['call_back'][call.data],
                     reply_markup=reply)


@bot.message_handler(func=lambda message: True, content_types=LOCATION)
def stores_location(message: Message) -> None:
    lon: float = message.location.longitude
    lat: float = message.location.latitude

    distance: List[...] = []
    for loc in STORES:
        result: float = vincenty((loc['lats'], loc['lons']), (lat, lon)).kilometers
        distance.append(result)
    index = distance.index(min(distance))
    bot.send_message(message.chat.id, MESSAGE['nearest_store'])
    bot.send_venue(message.chat.id,
                   STORES[index]['lats'],
                   STORES[index]['lons'],
                   STORES[index]['title'],
                   STORES[index]['address'])

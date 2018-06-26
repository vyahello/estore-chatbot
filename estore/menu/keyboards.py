from abc import ABC, abstractmethod
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from estore.menu.buttons import Buttons, KeyboardButtons

markup_inline_payment = InlineKeyboardMarkup()
btn_in_cash = InlineKeyboardButton('Cash', callback_data='cash')
btn_in_card = InlineKeyboardButton('Bank card', callback_data='card')
btn_in_invoice = InlineKeyboardButton('Bank transaction', callback_data='invoice')
markup_inline_payment.add(btn_in_cash, btn_in_card, btn_in_invoice)


class Keyboard(ABC):
    """Abstraction of keyboard."""

    @abstractmethod
    def reply(self) -> ReplyKeyboardMarkup:
        pass


class BotKeyboardMarkup(Keyboard):
    """Chat bot keyboard markup."""

    def __init__(self, resize_keyboard: bool, row_width: int) -> None:
        self._reply_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard,
                                                                        row_width=row_width)

    def reply(self) -> ReplyKeyboardMarkup:
        return self._reply_keyboard


class Menu(ABC):
    """Abstraction of keyboard menu."""

    @abstractmethod
    def request_button(self) -> None:
        pass


class MarkUpKeyboardMenu(Menu):
    """Chat bot markup menu with reply request_button."""

    def __init__(self) -> None:
        self._buttons: Buttons = KeyboardButtons()
        self._reply_keyboard: Keyboard = BotKeyboardMarkup(resize_keyboard=True, row_width=1)

    def request_button(self) -> None:
        self._reply_keyboard.reply().add(self._buttons.stores(), self._buttons.payment(), self._buttons.delivery())

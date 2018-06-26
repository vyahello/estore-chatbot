from abc import ABC, abstractmethod
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class Button(ABC):
    """Abstraction of keyboard reply."""

    @abstractmethod
    def stores(self) -> KeyboardButton:
        pass

    @abstractmethod
    def payment(self) -> KeyboardButton:
        pass

    @abstractmethod
    def delivery(self) -> KeyboardButton:
        pass


class Menu(ABC):
    """Abstraction of keyboard menu."""

    @abstractmethod
    def reply(self) -> None:
        pass


class MenuButton(Button):
    """Chatbot menu reply."""

    def __init__(self) -> None:
        self._stores: KeyboardButton = KeyboardButton('Stores addresses', request_location=True)
        self._payment: KeyboardButton = KeyboardButton('Payment methods')
        self._delivery: KeyboardButton = KeyboardButton('Delivery methods')

    def stores(self) -> KeyboardButton:
        return self._stores

    def payment(self) -> KeyboardButton:
        return self._payment

    def delivery(self) -> KeyboardButton:
        return self._delivery


class MarkUpMenu(Menu):
    """Chatbot markup menu with reply buttons."""

    def __init__(self) -> None:
        self._reply_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        self._button: Button = MenuButton()

    def reply(self) -> None:
        self._reply_keyboard.add(self._button.stores(), self._button.delivery(), self._button.payment())

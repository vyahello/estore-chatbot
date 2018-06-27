from abc import ABC, abstractmethod
from telebot.types import ReplyKeyboardMarkup
from estore.options.keyboards import InlineKeyboard, Keyboard, RequestKeyboard, ReplyInlineKeyboard


class Menu(ABC):
    """Abstraction of keyboard menu."""

    @abstractmethod
    def requests(self) -> ReplyKeyboardMarkup:
        pass

    @abstractmethod
    def replies(self) -> InlineKeyboard:
        pass


class MarkUpKeyboardMenu(Menu):
    """Chat bot markup menu with reply button."""

    def __init__(self, keyboard: Keyboard) -> None:
        self._request_keyboard: RequestKeyboard = RequestKeyboard(keyboard)
        self._reply_keyboard: InlineKeyboard = ReplyInlineKeyboard(keyboard)

    def requests(self) -> None:
        return self._request_keyboard.requests()

    def replies(self) -> InlineKeyboard:
        return self._reply_keyboard

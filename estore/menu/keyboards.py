from abc import ABC, abstractmethod
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from estore.menu.buttons import RequestButtons, RequestKeyboardButtons, ReplyButtons, ReplyKeyboardButtons


class Keyboard(ABC):
    """Abstraction of keyboard."""

    @abstractmethod
    def reply_keyboard(self) -> ReplyKeyboardMarkup:
        pass

    @abstractmethod
    def inline_keyboard(self) -> InlineKeyboardMarkup:
        pass


class InlineKeyboard(ABC):
    """Abstraction of an inline keyboard."""

    @abstractmethod
    def stores(self) -> InlineKeyboardMarkup:
        pass

    @abstractmethod
    def payment(self) -> InlineKeyboardMarkup:
        pass

    @abstractmethod
    def delivery(self) -> InlineKeyboardMarkup:
        pass


class Menu(ABC):
    """Abstraction of keyboard menu."""

    @abstractmethod
    def requests(self) -> ReplyKeyboardMarkup:
        pass

    @abstractmethod
    def replies(self) -> InlineKeyboardMarkup:
        pass


class BotKeyboard(Keyboard):
    """Chat bot keyboard markup."""

    def __init__(self, resize_keyboard: bool, row_width: int) -> None:
        self._reply_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=resize_keyboard,
                                                                        row_width=row_width)
        self._inline_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()

    def reply_keyboard(self) -> ReplyKeyboardMarkup:
        return self._reply_keyboard

    def inline_keyboard(self) -> InlineKeyboardMarkup:
        return self._inline_keyboard


class ReplyInlineKeyboard(InlineKeyboard):
    """Concrete reply inline keyboard"""

    def __init__(self, keyboard: Keyboard) -> None:
        self._reply_btn: ReplyButtons = ReplyKeyboardButtons()
        self._keyboard: Keyboard = keyboard

    def stores(self) -> InlineKeyboardMarkup:
        self._keyboard.inline_keyboard().add(self._reply_btn.stores().nearest())
        return self._keyboard.inline_keyboard()

    def payment(self) -> InlineKeyboardMarkup:
        self._keyboard.inline_keyboard().add(self._reply_btn.payment().card(),
                                             self._reply_btn.payment().cash(),
                                             self._reply_btn.payment().invoice())
        return self._keyboard.inline_keyboard()

    def delivery(self) -> InlineKeyboardMarkup:
        self._keyboard.inline_keyboard().add(self._reply_btn.delivery().post_office(),
                                             self._reply_btn.delivery().courier())
        return self._keyboard.inline_keyboard()


class RequestKeyboard:
    """Represent request keyboard."""

    def __init__(self, keyboard: Keyboard):
        self._keyboard: Keyboard = keyboard
        self._request_btn: RequestButtons = RequestKeyboardButtons()

    def requests(self) -> None:
        self._keyboard.reply_keyboard().add(self._request_btn.stores(),
                                            self._request_btn.payment(),
                                            self._request_btn.delivery())


class MarkUpKeyboardMenu(Menu):
    """Chat bot markup menu with reply button."""

    def __init__(self) -> None:
        keyboard: Keyboard = BotKeyboard(resize_keyboard=True, row_width=1)
        self._reply_keyboard: InlineKeyboard = ReplyInlineKeyboard(keyboard)
        self._request_keyboard: RequestKeyboard = RequestKeyboard(keyboard)

    def requests(self) -> None:
        return self._request_keyboard.requests()

    def replies(self) -> InlineKeyboard:
        return self._reply_keyboard

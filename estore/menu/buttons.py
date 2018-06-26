from typing import Any
from abc import ABC, abstractmethod
from telebot.types import KeyboardButton


class Button(ABC):
    """Abstraction of keyboard button."""

    @abstractmethod
    def view(self) -> KeyboardButton:
        pass


class Buttons(ABC):
    """Abstraction of keyboard request_button."""

    @abstractmethod
    def stores(self) -> KeyboardButton:
        pass

    @abstractmethod
    def payment(self) -> KeyboardButton:
        pass

    @abstractmethod
    def delivery(self) -> KeyboardButton:
        pass


class MenuButton(Button):
    """Specific menu button."""

    def __init__(self, name: str, **kwargs: Any) -> None:
        self._button: KeyboardButton = KeyboardButton(name, kwargs)

    def view(self) -> KeyboardButton:
        return self._button


class KeyboardButtons(Buttons):
    """Specific keyboard request_button."""

    def __init__(self) -> None:
        self._stores: Button = MenuButton(name='Stores addresses', request_location=True)
        self._payment: Button = MenuButton(name='Payment methods')
        self._delivery: Button = MenuButton(name='Delivery methods')

    def stores(self) -> KeyboardButton:
        return self._stores.view()

    def payment(self) -> KeyboardButton:
        return self._payment.view()

    def delivery(self) -> KeyboardButton:
        return self._delivery.view()

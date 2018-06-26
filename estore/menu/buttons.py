from typing import Any
from abc import ABC, abstractmethod
from telebot.types import KeyboardButton, InlineKeyboardButton, JsonSerializable


class Button(ABC):
    """Abstraction of keyboard button."""

    @abstractmethod
    def view(self) -> JsonSerializable:
        pass


class RequestButtons(ABC):
    """Abstraction of keyboard request button."""

    @abstractmethod
    def stores(self) -> JsonSerializable:
        pass

    @abstractmethod
    def payment(self) -> JsonSerializable:
        pass

    @abstractmethod
    def delivery(self) -> JsonSerializable:
        pass


class StoreReplyButton(object):
    """Reply buttons on ``Store`` button request"""

    def __init__(self) -> None:
        self._nearest_btn: Button = ReplyButton('Nearest', 'nearest')

    def nearest(self) -> JsonSerializable:
        return self._nearest_btn.view()


class PaymentReplyButton(object):
    """Reply buttons on ``Payment`` button request"""

    def __init__(self) -> None:
        self._cash_btn: Button = ReplyButton('Cash', 'cash')
        self._card_btn: Button = ReplyButton('Bank card', 'card')
        self._invoice_btn: Button = ReplyButton('Bank transaction', 'invoice')

    def cash(self) -> JsonSerializable:
        return self._cash_btn.view()

    def card(self) -> JsonSerializable:
        return self._card_btn.view()

    def invoice(self) -> JsonSerializable:
        return self._invoice_btn.view()


class DeliveryReplyButton(object):
    """Reply buttons on ``Delivery`` button request"""

    def __init__(self) -> None:
        self._courier_btn: Button = ReplyButton('Courier delivery', 'courier delivery')
        self._post_office_btn: Button = ReplyButton('Post Office', 'post office')

    def courier(self) -> JsonSerializable:
        return self._courier_btn.view()

    def post_office(self) -> JsonSerializable:
        return self._post_office_btn.view()


class ReplyButtons(ABC):
    """Abstraction of keyboard reply button."""

    @abstractmethod
    def stores(self) -> StoreReplyButton:
        pass

    @abstractmethod
    def payment(self) -> PaymentReplyButton:
        pass

    @abstractmethod
    def delivery(self) -> DeliveryReplyButton:
        pass


class ReplyKeyboardButtons(ReplyButtons):
    """Specific keyboard request_button."""

    def __init__(self) -> None:
        self._stores: StoreReplyButton = StoreReplyButton()
        self._payment: PaymentReplyButton = PaymentReplyButton()
        self._delivery: DeliveryReplyButton = DeliveryReplyButton()

    def stores(self) -> StoreReplyButton:
        return self._stores

    def payment(self) -> PaymentReplyButton:
        return self._payment

    def delivery(self) -> DeliveryReplyButton:
        return self._delivery


class ReplyButton(Button):
    """Specific reply menu button."""

    def __init__(self, name: str, callback_data: str) -> None:
        self._button: JsonSerializable = InlineKeyboardButton(name, callback_data=callback_data)

    def view(self) -> JsonSerializable:
        return self._button


class RequestButton(Button):
    """Specific request menu button."""

    def __init__(self, name: str, **kwargs: Any) -> None:
        self._button: JsonSerializable = KeyboardButton(name, kwargs)

    def view(self) -> JsonSerializable:
        return self._button


class RequestKeyboardButtons(RequestButtons):
    """Specific keyboard request_button."""

    def __init__(self) -> None:
        self._stores: Button = RequestButton(name='Stores addresses', request_location=True)
        self._payment: Button = RequestButton(name='Payment methods')
        self._delivery: Button = RequestButton(name='Delivery methods')

    def stores(self) -> JsonSerializable:
        return self._stores.view()

    def payment(self) -> JsonSerializable:
        return self._payment.view()

    def delivery(self) -> JsonSerializable:
        return self._delivery.view()

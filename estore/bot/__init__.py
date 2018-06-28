from typing import Tuple, List, Dict, Any

API_TOKEN: str = '550173812:AAG9eR9G-jLvfKAgTGzZMAPL4IdlAb1jjWc'
COMMANDS: Tuple[str, ...] = ('start', 'help')

LOCATION: List[str] = ['location']

MESSAGE: Dict[Any, Any] = {
    'welcome': "Hey! I'm a bot of an Estore, how can i help you?",
    'error': "Sorry I can't figure our your request, please use buttons below!",
    'delivery': {
        'methods': 'Delivery methods', 'reply': 'Here are next delivery methods', 'call_back': {
            'courier delivery': 'Our courier can easily deliver the deed right upon your home',
            'post office': 'You can pick up your deed in a post office'
        }
    },
    'payment': {
        'methods': 'Payment methods', 'reply': 'Here are next payment methods', 'call_back': {
            'cash': 'Cash payment is conducted in store counter in USD',
            'card': 'Bank card payment is conducted with your VISA/Mastercard',
            'invoice': 'You can pay for a deed with your bank transaction'
        }
    },
    'nearest_store': 'Here is a nearest store according to your location'
}

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

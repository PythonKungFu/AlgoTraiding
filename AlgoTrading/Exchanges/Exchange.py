import requests
from keys import *


class Exchange:
    base_url = ''
    TOKENTG = TOKENTELEGRAM
    USERTG = USERTELEGRAM

    def any_request(self, method, params=None):
        return requests.get(self.base_url + method, params=params).json()

    def send_message_telegram(self, message):
        url = f"https://api.telegram.org/bot{self.TOKENTG}/sendMessage"
        data = {
            'chat_id': self.USERTG,
            'text': message
        }
        return requests.post(url, data=data).json()

    def exchange_info(self):
        return self.any_request(method=None)

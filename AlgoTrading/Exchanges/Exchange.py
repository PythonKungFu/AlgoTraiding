import requests
from keys import *


class Exchange:
    base_url = ''
    TOKENTG = TOKENTELEGRAM
    USERTG = USERTELEGRAM

    def any_request(self, method: str, params=None):
        """ Отправляем любой запрос с параметрами """
        return requests.get(self.base_url + method, params=params).json()

    def send_message_telegram(self, message: str):
        """" Отправляем сообщение в телеграм"""
        url = f"https://api.telegram.org/bot{self.TOKENTG}/sendMessage"
        data = {
            'chat_id': self.USERTG,
            'text': message
        }
        return requests.post(url, data=data).json()

    def exchange_info(self) -> dict:
        """" Получаем общую информацию по бирже """
        return self.any_request(method=None)

    def get_trade_list(self, coin: str) -> list:
        """" Получаем список последних сделок """
        return self.any_request(method=None)

    def ticker_24hr_price_change(self, symbol: str) -> dict:
        """" Получаем статистику изменения цен за 24 часа"""
        pass

    def get_symbol_price(self, symbol: str, rounding: int) -> float:
        """" Получаем цену монеты """
        pass

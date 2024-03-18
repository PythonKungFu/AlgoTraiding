import requests
from AlgoTrading.Exchanges.Exchange import Exchange


class Commex(Exchange):
    base_url = 'https://api.commex.com/api/v1/'

    def any_request(self, method, params=None):
        return super().any_request(**{'method': method, 'params': params})

    def exchange_info(self):
        return self.any_request('exchangeInfo')

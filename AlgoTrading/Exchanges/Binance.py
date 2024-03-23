from AlgoTrading.Exchanges.Exchange import Exchange


class Binance(Exchange):
    base_url = "https://api.binance.com/api/v3/"

    def any_request(self, method, params=None):
        return super().any_request(**{'method': method, 'params': params})

    def exchange_info(self):
        return self.any_request('exchangeInfo')

    def get_trade_list(self, coin, limit=None):
        params = {
            'symbol': coin,
            'limit': limit  # max - 1000
        }
        return self.any_request('trades', params=params)

from AlgoTrading.Exchanges.Exchange import Exchange
from multiprocessing.dummy import Pool as ThreadPool


class Commex(Exchange):
    base_url = 'https://api.commex.com/api/v1/'

    def any_request(self, method, params=None):
        return super().any_request(**{'method': method, 'params': params})

    def exchange_info(self):
        return self.any_request('exchangeInfo')

    def ticker_24hr_price_change(self, symbol):
        return self.any_request(method='ticker/24hr', params={'symbol': symbol})

    def tickers_24hr_price_change(self):
        """" Возвращает список изменений цен за 24 часа"""
        info = self.exchange_info()
        tickers = []
        for symbol in info['symbols']:
            if symbol['symbol'].endswith('USDT'):
                tickers.append(symbol['symbol'])

        pool = ThreadPool(12)
        tickers_change = pool.map(self.ticker_24hr_price_change, tickers)
        return tickers_change



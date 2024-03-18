""""
Документация Binance:

https://binance-docs.github.io/apidocs/spot/en/#change-log

Задача:

- установить библиотеку Requests https://pypi.org/project/requests/

```python
import requests
import pprint

ticker = requests.get('https://api.binance.com/api/v3/ticker/price')
result = ticker.json()
pprint.pprint(result)
```

- в коде выше отсортировать монеты, чтобы в выдаче остались только тикеры, которые оканчиваются на ‘USDT’.
"""
import requests
from pprint import pp


tickers = requests.get('https://api.binance.com/api/v3/ticker/price').json()
result_tickers = []

for ticker in tickers:
    if ticker['symbol'].endswith('USDT'):
        result_tickers.append(ticker)

pp(result_tickers)

import time

from AlgoTrading.Exchanges.Binance import Binance


"""" 
Нужно установить написать скрипт, который будет сигнализировать в телеграм, когда цена преодолеет определенный уровень.
"""

SYMBOL = 'BTCUSDT'
LEVEL = 65530

binance = Binance()

while True:
    price = binance.get_trade_list(SYMBOL, limit=1)[0]['price']
    if float(price) > LEVEL:
        message = SYMBOL + '  Price!!! : ' + price
        binance.send_message_telegram(message)
        print(f"{price} > {LEVEL}")
        break
    else:
        print("search " + price)
    time.sleep(5)

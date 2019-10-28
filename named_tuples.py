from collections import namedtuple
import datetime

StockPrice = namedtuple('StockPrice',
['symbol', 'date', 'closing_price'])

price = StockPrice('MSFT', datetime.date(2018, 12, 14), 106.03)
assert price.symbol == 'MSFT'
assert price.closing_price == 106.03

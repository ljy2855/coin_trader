from module.RealtimePricePaser import RealtimePrice
import pyupbit
from module.RealtimePricePaser import market_code


class BitCoinAPI():
    def __init__(self):
        self.real_time_thread = RealtimePrice()
        self.real_time_thread.daemon = True
        self.setPrevData()

    def setPrevData(self):
        self.prev_data = pyupbit.get_ohlcv(
            market_code, interval="minute1", count=100)
        self.prev_data.rename(columns={'opening_price': 'Open',
                                       'high_price': 'High',
                                       'low_price': 'Low',
                                       'trade_price': 'Close',
                                       'candle_acc_trade_volume': 'Volume',
                                       }, inplace=True)
        self.prev_data.index.name = "Date"

    def startParsingRealTimePrice(self):
        self.real_time_thread.start()

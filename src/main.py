import pyupbit
import mplfinance as mpf
from threading import Thread
market_code = "KRW-BTC"


class BitCoinAPI():
    def __init__(self):
        self.real_time_thread = RealtimePrice()
        self.real_time_thread.daemon = True

    def initChart(self):
        self.setPrevData()
        mpf.plot(self.prev_data, type='candle', mav=(3, 6, 9), volume=True)

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


class RealtimePrice(Thread):

    def run(self):
        websocket_manager = pyupbit.WebSocketManager("ticker", [market_code])
        while True:
            data = websocket_manager.get()
            print(data['trade_price'])
            self.ticker = data


if __name__ == '__main__':

    try:
        bit = BitCoinAPI()
        # bit.startParsingRealTimePrice()
        bit.initChart()
        print(bit.prev_data)
        input()
    except KeyboardInterrupt:
        pass

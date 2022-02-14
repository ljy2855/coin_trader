import time
import numpy as np
import pandas as pd
import pyupbit
import mplfinance as mpf
from threading import Thread


market_code = "KRW-BTC"


class BitCoinAPI():
    def __init__(self):
        self.real_time_thread = RealtimePrice()
        self.real_time_thread.daemon = True
        self.setPrevData()

    def initChart(self):

        mpf.plot(self.prev_data,  type='candle',
                 mav=(3, 6, 9), volume=True)

        mpf.show()

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
        self.data_dict = dict()  # {'timestamp' : array([price...])}
        self.start_time = None

        while True:
            data = websocket_manager.get()
            self.manageDataFrame(data)

    def manageDataFrame(self, data):

        # pyupbit lib edited for optimization
        #trading_price = data['trading_price']
        #trading_volume = data['trading_volume']
        #timestamp = data['timestamp'] / 1000

        trading_price = data['tp']
        trading_volume = data['tv']
        timestamp = data['tms'] / 1000

        if self.start_time == None:  # init
            self.start_time = timestamp
            self.minute_ticker = []
            self.volume = 0
        else:
            if self.start_time + 10 <= timestamp:  # 60초마다 price,volume 저장
                self.data_dict.update({timestamp: {'prices': np.array(self.minute_ticker),
                                                   'volume': self.volume}})
                self.start_time = timestamp
                print(self.data_dict)
                self.minute_ticker = []
                self.volume = 0
            self.minute_ticker.append(int(trading_price))
            self.volume += trading_volume


if __name__ == '__main__':

    bit = BitCoinAPI()
    bit.startParsingRealTimePrice()
    time.sleep(3)
    # bit.initChart()

    # print(bit.prev_data)
    time.sleep(1000)

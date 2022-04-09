from threading import Thread
import numpy as np
import pyupbit

market_code = "KRW-BTC"
parse_priod = 10


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
            if self.start_time + parse_priod <= timestamp:  # 60초마다 price,volume 저장
                self.data_dict.update({timestamp: {'prices': np.array(self.minute_ticker),
                                                   'volume': self.volume}})
                self.start_time = timestamp
                print(self.data_dict)
                self.minute_ticker = []
                self.volume = 0
            self.minute_ticker.append(int(trading_price))
            self.volume += trading_volume

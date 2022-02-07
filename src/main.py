import pyupbit
import time
from threading import Timer 

market_code = "KRW-BTC"

class RepeatTimer(Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):  
            self.function(*self.args,**self.kwargs)  

class BitCoinAPI():
    
    def __init__(self):
        self.bit_data = pyupbit.get_ohlcv(market_code,interval="minute1", count=100)
        self.price = pyupbit.get_current_price(market_code) 
        self.thread = RepeatTimer(2,self.updatePrice)
        
        
    def startUpdatePrice(self):
        self.thread.start()
        
    def updatePrice(self):
        self.price = pyupbit.get_current_price(market_code) 
        print(self.price)
    
    def getPrice(self):
        return self.price


if __name__ == '__main__':
    try:
        bit = BitCoinAPI()
        print(bit.bit_data)
        bit.startUpdatePrice()
        time.sleep(100)
    except KeyboardInterrupt:
        pass
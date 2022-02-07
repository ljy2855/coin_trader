import time
import requests
from urllib import parse
from threading import Timer, Thread, Event
repeat_time = 2

class BitCoinAPI:

    def __init__(self):
        self.market_code = "KRW-BTC"
        self.base_url = "https://api.upbit.com/v1"
        self.stopFlag = Event()
        self.parse_thread = Timer(1, self.getCurrentTicker)


    def startParse(self):

        self.parse_thread.start()

    def getCurrentTicker(self):
        headers = {"Accept": "application/json"}
        url = parse.urljoin(self.base_url, '/ticker?markets=' + self.market_code)
        response = requests.request("GET", url, headers=headers)


if __name__ == "__main__":
    bit = BitCoinAPI()
    bit.startParse()

    time.sleep(10)

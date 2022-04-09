import time

from module.BitCoinAPI import BitCoinAPI


if __name__ == '__main__':

    bit = BitCoinAPI()
    bit.startParsingRealTimePrice()
    time.sleep(3)
    # bit.initChart()

    print(bit.prev_data)
    time.sleep(1000)

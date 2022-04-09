import time
from AuthHeader import getAuthHeader, getTradeHeader
import requests
from collections import deque

server_url = "https://api.upbit.com"


class UserAPI():

    def __init__(self) -> None:
        self.orders = deque()
        self.is_hold = False
        self.is_ordering = False
        self.balance = 0.0
        self.money = 0.0

    def updateAccount(self) -> None:
        account_data = self.getAccount()
        try:
            self.money = account_data[0]['balance']
            self.balance = account_data[1]['balance']
            self.is_hold = True
        except IndexError:  # 코인 보유 x
            self.balance = 0.0
            self.is_hold = False
        except TypeError:  # API call fail
            time.sleep(1)
            self.updateAccount()
        print(self.balance)
        print(self.money)

    def getAccount(self):
        try:
            res = requests.get(server_url + "/v1/accounts",
                               headers=getAuthHeader())
            if res.status_code == 200:
                return res.json()

        except e:
            print(e)

    def buyCoin(self, volume: float, price: float, order_type: str):
        query = {
            'market': 'KRW-BTC',
            'side': 'bid',
            'volume': str(volume),
            'price': str(price),
            'ord_type': order_type,
        }
        try:
            res = requests.post(server_url + "/v1/orders",
                                params=query, headers=getTradeHeader(query=query))
            if res.status_code == 201:
                data = res.json()
                self.orders.append(data)

        except e:
            print(e)

    def sellCoin(self, volume: float, price: float, order_type: str):
        query = {
            'market': 'KRW-BTC',
            'side': 'ask',
            'volume': str(volume),
            'price': str(price),
            'ord_type': order_type,
        }
        try:
            res = requests.post(server_url + "/v1/orders",
                                params=query, headers=getTradeHeader(query=query))
            if res.status_code == 201:
                data = res.json()
                self.orders.append(data)

        except e:
            print(e)

    def getLastOrderUUID(self) -> str:
        if not self.orders:
            return '0'
        return self.orders[-1]['uuid']

    def checkOrderStatus(self):
        pass


if __name__ == '__main__':
    api = UserAPI()
    api.updateAccount()

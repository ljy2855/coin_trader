from AuthHeader import getAuthHeader
import requests

server_url = "https://api.upbit.com"


class UpbitAPI():
    def __init__(self):
        self.header = getAuthHeader()

    def checkAccount(self):
        try:
            res = requests.get(server_url + "/v1/accounts",
                               headers=self.header)
            data = res.json()
            print(data)

        except e:
            print(e)


if __name__ == '__main__':
    api = UpbitAPI()
    api.checkAccount()

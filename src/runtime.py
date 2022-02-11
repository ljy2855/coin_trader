import websockets 
import asyncio
import json
from pyupbit import WebSocketManager
'''
async def upbit_ws_clinet():
    uri = "wss://api.upbit.com/websocket/v1"
    
    async with websockets.connect(uri, ping_interval=60) as websocket:
        subscribe_fmt = [
            {"ticket":"test"},
            {
                "type": "ticker",
                "codes":["KRW-BTC"],
                "isOnlyRealtime": True
            },
            {"format":"SIMPLE"}
        ]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)
        
        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)
            
async def main():
    await upbit_ws_clinet()
'''
if __name__ == '__main__':
    wm = WebSocketManager("ticker", ["KRW-BTC"])
    while True:
        data = wm.get()
        print(data)
        recv = data
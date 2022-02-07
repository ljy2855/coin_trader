import websockets
import asyncio
import json

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
        
        while Ture:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)
            
async def main():
    await upbit_ws_clinet()

asyncio.run(main())
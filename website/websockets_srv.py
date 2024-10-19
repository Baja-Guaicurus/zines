import serial
import asyncio
from websockets.asyncio.server import serve

ser = serial.Serial('/dev/ttyUSB0')

async def get_string(websocket):
    while True:
        data = str(ser.readline())
        data = data.decode()
        data = data[:2]
        await websocket.send(data)


async def main():
    async with serve(get_string, "localhost", 12345):
        await asyncio.get_running_loop().create_future()

asyncio.run(main())

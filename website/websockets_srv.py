import serial
import asyncio
from websockets.asyncio.server import serve
from sys import exit

port = "/dev/ttyUSB0"
try:
    ser = serial.Serial(port)
except:
    print(f"{port} inacessível")
    exit(1)

async def get_string(websocket):
    while True:
        data = ser.readline()
        data = data.decode()
        data = data[:-2]
        print(data)
        await websocket.send(data)

async def main():
    async with serve(get_string, "localhost", 12345):
        await asyncio.get_running_loop().create_future()

asyncio.run(main())

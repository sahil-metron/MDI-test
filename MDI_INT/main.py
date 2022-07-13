import asyncio
import os
import signal
import websockets


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            break
        print(message)


# async def main():
#     async with websockets.serve(handler,'0.0.0.0', 8001):
#         await asyncio.Future()  # run forever

async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    port = int(os.environ.get("PORT", "8001"))
    print(port)
    print(handler)
    async with websockets.serve(handler, "", port):
        await stop

if __name__ == "__main__":
    asyncio.run(main())

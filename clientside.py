import asyncio
import websockets


async def connect_to_server():
    async with websockets.connect("ws://localhost:8000") as websocket:
        message = "Hello "

        await websocket.send(message)
        print("Message sent to server.")

        # Wait for the server's response
        response = await websocket.recv()
        print(f"Received response from server: {response}")


asyncio.get_event_loop().run_until_complete(connect_to_server())

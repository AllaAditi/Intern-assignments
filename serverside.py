import asyncio
import websockets


async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")

        # Process the message from the client

        # Send a response back to the client
        response = f"Server received: {message}"
        await websocket.send(response)


start_server = websockets.serve(handle_client, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

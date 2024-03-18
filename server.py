import asyncio
import websockets
import pyautogui
import io
from PIL import Image
import mss

async def screen_capture(websocket, path):
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Capture the first monitor

        while True:
            try:
                # Capture the screen
                sct_img = sct.grab(monitor)

                # Convert the screenshot to bytes
                img_bytes = sct_img.rgb

                # Create a PIL Image from bytes
                image = Image.frombytes("RGB", sct_img.size, img_bytes)

                # Convert the image to bytes in PNG format
                with io.BytesIO() as output:
                    image.save(output, format='PNG')
                    img_byte_arr = output.getvalue()

                # Send the screenshot to the client
                await websocket.send(img_byte_arr)

            except Exception as e:
                print(f"An error occurred: {e}")
                break

# Replace '192.168.8.199' with your server's IP address
start_server = websockets.serve(screen_capture, '192.168.8.199', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

import asyncio
import websockets
from PIL import Image, ImageTk
import io
import tkinter as tk
import time

async def receive_screen(root, canvas, uri="ws://192.168.8.199:5678", fps=30):
    last_frame_time = time.time()
    frame_duration = 1.0 / fps

    async with websockets.connect(uri) as websocket:
        while True:
            now = time.time()
            elapsed_time = now - last_frame_time

            if elapsed_time >= frame_duration:
                img_data = await websocket.recv()
                image = Image.open(io.BytesIO(img_data))
                tk_image = ImageTk.PhotoImage(image)
                if hasattr(canvas, 'image_id'):
                    canvas.itemconfig(canvas.image_id, image=tk_image)
                else:
                    canvas.image_id = canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
                canvas.image = tk_image
                root.update_idletasks()  # Update the canvas
                root.update()  # Update the Tkinter GUI
                last_frame_time = now

def main():
    root = tk.Tk()
    root.title("Screen Monitor")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

    canvas = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas.pack()

    asyncio.get_event_loop().run_until_complete(receive_screen(root, canvas))

if __name__ == "__main__":
    main()

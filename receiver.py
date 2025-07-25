# gui_app.py
import tkinter as tk
import threading
import time
import requests

API_URL = "https://resplendent-fairy-d0f38f.netlify.app"

def poll_orders():
    while True:
        try:
            response = requests.get("https://resplendent-fairy-d0f38f.netlify.app")  # Optional endpoint for future
            if response.ok:
                data = response.json()
                if data:
                    order_text = f"From: {data['name']}\nOrder: {data['order']}\n\n"
                    text_widget.insert(tk.END, order_text)
        except:
            pass
        time.sleep(2)

app = tk.Tk()
app.title("Order Receiver")
text_widget = tk.Text(app, height=20, width=60)
text_widget.pack(padx=20, pady=20)

# You can also just monitor the console from api_server.py or share the queue.
threading.Thread(target=poll_orders, daemon=True).start()

app.mainloop()

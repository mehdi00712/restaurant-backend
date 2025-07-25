# order_viewer.py
import tkinter as tk
import threading
import requests
import time

# 🔁 Replace this with your live Render API URL
RENDER_API_URL = "https://restaurant-backend-uyq0.onrender.com"

def fetch_orders():
    while True:
        try:
            response = requests.get(RENDER_API_URL)
            if response.ok:
                data = response.json()
                if data:
                    order = f"🧾 New Order\nName: {data.get('name')}\nOrder: {data.get('order')}\n{'-'*40}\n"
                    output.insert(tk.END, order)
                    output.see(tk.END)
        except Exception as e:
            output.insert(tk.END, f"⚠️ Error: {e}\n")
        time.sleep(5)

# 🖥️ GUI Setup
app = tk.Tk()
app.title("🍽️ Live Restaurant Orders")
app.geometry("500x400")

output = tk.Text(app, wrap="word", bg="#f8f8f8", fg="#333", font=("Arial", 12))
output.pack(padx=10, pady=10, fill="both", expand=True)

# 🔁 Start background order checking thread
threading.Thread(target=fetch_orders, daemon=True).start()

app.mainloop()

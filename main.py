import customtkinter as ctk
from db import get_all_data
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("600x600")
app.title("MongoDB Viewer")

label = ctk.CTkLabel(app, text="📡 Waiting for data...")
label.pack(pady=20)

def fetch_users():
    print("Fetching users from DB...")
    users = get_all_data()
    
    # 🧠 Format data nicely
    data_text = "\n".join([str(user) for user in users])

    # 🪄 Update label on the main thread
    app.after(0, lambda: label.configure(text=data_text))

def start_function():
    threading.Thread(target=fetch_users).start()  # ✅ Thread-safe fetching

btn = ctk.CTkButton(
    master=app,
    text="Launch 🚀",
    fg_color="#2a2a40",
    hover_color="#444",
    text_color="white",
    corner_radius=10,
    font=("Verdana", 16, "bold"),
    command=start_function
)
btn.pack(pady=12)

app.mainloop()

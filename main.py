import customtkinter as ctk
from db import get_all_data
import threading
from db import insert_data


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("700x600")
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
    text="show logs",
    fg_color="#2a2a40",
    hover_color="#444",
    text_color="white",
    corner_radius=10,
    font=("Verdana", 16, "bold"),
    command=start_function
)
btn.pack(pady=12)


def getuserentry():
    print("User entry function called")
    username=entry.get()
    password=entry2.get()
    email=entry3.get()
    label2.configure(text=f"Welcome, {username} 🔥")
    label3.configure(text=f"email:{email}")
    label4.configure(text=f"password:{password}")
    print(username)

    user={"name": username, "password": password, "email": email}
    insert_id=insert_data(user)
    print("data inserted ",insert_id)


entry = ctk.CTkEntry(app, placeholder_text="enter username", width=300, height=40)
entry.pack(pady=5)

entry2 = ctk.CTkEntry(app, placeholder_text="enter password", width=300, height=40)
entry2.pack(pady=5)

entry3 = ctk.CTkEntry(app, placeholder_text="enter email", width=300, height=40)
entry3.pack(pady=5)


btn = ctk.CTkButton(
    master=app,
    text="Submit 🚀",
    command=getuserentry,
    font=("Verdana", 14, "bold"),
    fg_color="#1f1f1f",
    hover_color="#333",
    text_color="white",
)
btn.pack(pady=10)

# 📺 Label to display result
label2 = ctk.CTkLabel(app, text="")
label2.pack(pady=10)
label3 = ctk.CTkLabel(app,text="")
label3.pack(pady=10)
label4 = ctk.CTkLabel(app,text="")
label4.pack(pady=10)

print(entry)

app.mainloop()

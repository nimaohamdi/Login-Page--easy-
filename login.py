import tkinter as tk
from tkinter import messagebox

# Hardcoded credentials for demo
USERNAME = "admin"
PASSWORD = "1234"

# Login function
def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == USERNAME and entered_password == PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome, " + USERNAME + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")
root.configure(bg="#f2f2f2")

# Username label and entry
tk.Label(root, text="Username:", bg="#f2f2f2").pack(pady=(20, 5))
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
tk.Label(root, text="Password:", bg="#f2f2f2").pack(pady=(10, 5))
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
tk.Button(root, text="Login", command=login, bg="#4CAF50", fg="white", width=10).pack(pady=20)

root.mainloop()

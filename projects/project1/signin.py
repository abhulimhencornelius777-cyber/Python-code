import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Simple check (you can improve this later)
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome " + username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create window
root = tk.Tk()
root.title("Sign In")
root.geometry("400x300")
root.configure(bg="#f0f2f5")  # light Facebook-like background

# Title
title = tk.Label(root, text="Sign In", font=("Arial", 20, "bold"), bg="#f0f2f5")
title.pack(pady=20)

# Username
entry_username = tk.Entry(root, width=30, font=("Arial", 12))
entry_username.insert(0, "Username")
entry_username.pack(pady=10)

# Password
entry_password = tk.Entry(root, width=30, font=("Arial", 12), show="*")
entry_password.insert(0, "Password")
entry_password.pack(pady=10)

# Login Button
login_btn = tk.Button(root, text="Log In", width=20, bg="#1877f2", fg="white", command=login)
login_btn.pack(pady=20)

# Run app
root.mainloop()

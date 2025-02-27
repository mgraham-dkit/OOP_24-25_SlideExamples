import tkinter as tk
from tkinter import messagebox
import json

root = tk.Tk()
root.title("Inventory System")
root.geometry("400x400")  # Set initial window size
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

inventory = {}
logged_in = False
users = {}


# Load data from files
def load_data():
    global inventory, users
    try:
        with open("inventory.txt", "r") as f:
            for line in f:
                item, qty = line.strip().split(":")
                inventory[item] = int(qty)
    except FileNotFoundError:
        inventory = {}

    try:
        with open("users.txt", "r") as f:
            for line in f:
                username, password = line.strip().split(":")
                users[username] = password
    except FileNotFoundError:
        users = {"admin": "password"}


# Save data to files
def save_data():
    with open("inventory.txt", "w") as f:
        for item, qty in inventory.items():
            f.write(f"{item}:{qty}\n")
    with open("users.txt", "w") as f:
        for username, password in users.items():
            f.write(f"{username}:{password}\n")


def register():
    username = reg_user_entry.get()
    password = reg_pass_entry.get()
    if username and password:
        if username in users:
            messagebox.showerror("Error", "User already exists")
        else:
            users[username] = password
            messagebox.showinfo("Success", "User registered successfully")
            register_frame.pack_forget()
            login_frame.pack(fill=tk.BOTH, expand=True)
    else:
        messagebox.showerror("Error", "Please enter both username and password")


def login():
    global logged_in
    username = user_entry.get()
    password = pass_entry.get()
    if username in users and users[username] == password:
        logged_in = True
        login_frame.pack_forget()
        inventory_frame.pack(fill=tk.BOTH, expand=True)
    else:
        messagebox.showerror("Error", "Invalid credentials")


def add_item():
    if not logged_in:
        messagebox.showerror("Error", "Please log in first")
        return
    item = item_entry.get()
    qty = qty_entry.get()
    if item and qty.isdigit():
        inventory[item] = inventory.get(item, 0) + int(qty)
        listbox.delete(0, tk.END)
        for item, qty in inventory.items():
            listbox.insert(tk.END, f"{item}: {qty}")
        item_entry.delete(0, tk.END)
        qty_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Invalid input")


def remove_item():
    if not logged_in:
        messagebox.showerror("Error", "Please log in first")
        return
    selected = listbox.curselection()
    if selected:
        item_text = listbox.get(selected[0])
        item_name = item_text.split(":")[0]
        if item_name in inventory:
            del inventory[item_name]
            listbox.delete(0, tk.END)
            for item, qty in inventory.items():
                listbox.insert(tk.END, f"{item}: {qty}")
    else:
        messagebox.showerror("Error", "Please select an item to remove")


def update_list():
    listbox.delete(0, tk.END)
    for item, qty in inventory.items():
        listbox.insert(tk.END, f"{item}: {qty}")


# Load data on startup
load_data()

# Register Frame
register_frame = tk.Frame(root, padx=10, pady=10)
reg_user_label = tk.Label(register_frame, text="New Username:")
reg_user_label.pack(fill=tk.X, padx=5, pady=2)
reg_user_entry = tk.Entry(register_frame)
reg_user_entry.pack(fill=tk.X, padx=5, pady=2)
reg_pass_label = tk.Label(register_frame, text="New Password:")
reg_pass_label.pack(fill=tk.X, padx=5, pady=2)
reg_pass_entry = tk.Entry(register_frame, show="*")
reg_pass_entry.pack(fill=tk.X, padx=5, pady=2)
register_button = tk.Button(register_frame, text="Register", command=register)
register_button.pack(fill=tk.X, padx=5, pady=2)

# Login Frame
login_frame = tk.Frame(root, padx=10, pady=10)
user_label = tk.Label(login_frame, text="Username:")
user_label.pack(fill=tk.X, padx=5, pady=2)
user_entry = tk.Entry(login_frame)
user_entry.pack(fill=tk.X, padx=5, pady=2)
pass_label = tk.Label(login_frame, text="Password:")
pass_label.pack(fill=tk.X, padx=5, pady=2)
pass_entry = tk.Entry(login_frame, show="*")
pass_entry.pack(fill=tk.X, padx=5, pady=2)
login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(fill=tk.X, padx=5, pady=2)
register_link = tk.Button(login_frame, text="Register",
                          command=lambda: (login_frame.pack_forget(), register_frame.pack(fill=tk.BOTH, expand=True)))
register_link.pack(fill=tk.X, padx=5, pady=2)
login_frame.pack(fill=tk.BOTH, expand=True)

# Inventory Frame
inventory_frame = tk.Frame(root, padx=10, pady=10)
item_label = tk.Label(inventory_frame, text="Item:")
item_label.pack(fill=tk.X, padx=5, pady=2)
item_entry = tk.Entry(inventory_frame)
item_entry.pack(fill=tk.X, padx=5, pady=2)
qty_label = tk.Label(inventory_frame, text="Quantity:")
qty_label.pack(fill=tk.X, padx=5, pady=2)
qty_entry = tk.Entry(inventory_frame)
qty_entry.pack(fill=tk.X, padx=5, pady=2)
add_button = tk.Button(inventory_frame, text="Add Item", command=add_item)
add_button.pack(fill=tk.X, padx=5, pady=2)
remove_button = tk.Button(inventory_frame, text="Remove Item", command=remove_item)
remove_button.pack(fill=tk.X, padx=5, pady=2)
listbox = tk.Listbox(inventory_frame)
listbox.pack(fill=tk.BOTH, padx=5, pady=2, expand=True)
for item, qty in inventory.items():
    listbox.insert(tk.END, f"{item}: {qty}")

# Save data on close
root.protocol("WM_DELETE_WINDOW", lambda: (save_data(), root.destroy()))

root.mainloop()

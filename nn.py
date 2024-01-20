import tkinter as tk
from tkinter import ttk
import shelve
import hashlib
from ttkbootstrap import Style

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def create_account():
    username = new_username_entry.get()
    password = new_password_entry.get()

    if not username or not password:
        status_label.config(text="Please enter both username and password.")
        return

    user_data = shelve.open("user_data", writeback=True)

    if username in user_data:
        status_label.config(text="Username already exists. Try a different one.")
    else:
        hashed_password = hash_password(password)
        user_data[username] = hashed_password
        user_data.close()
        status_label.config(text="Account created successfully.")

def show_main_page():
    main_page = tk.Toplevel(root)
    main_page.title("Main Page")
    main_page.geometry("400x300")  # Set your desired dimensions

    style = Style(theme="slate")  # Choose your preferred theme ("cyber", "cerulean", "slate", etc.)

    key_gen_button = ttk.Button(main_page, text="Key Generation", style="success.TButton", command=dummy_command)
    encrypt_button = ttk.Button(main_page, text="Encryption", style="primary.TButton", command=dummy_command)
    decrypt_button = ttk.Button(main_page, text="Decryption", style="warning.TButton", command=dummy_command)

    key_gen_button.pack(pady=10)
    encrypt_button.pack(pady=10)
    decrypt_button.pack(pady=10)

def login():
    username = username_entry.get()
    password = password_entry.get()

    user_data = shelve.open("user_data")
    stored_password = user_data.get(username, None)
    user_data.close()

    if stored_password is None:
        status_label.config(text="Invalid username. Please try again.")
    elif hash_password(password) == stored_password:
        status_label.config(text="Login successful.")
        show_main_page()
    else:
        status_label.config(text="Incorrect password. Please try again.")

def dummy_command():
    # Replace this function with the actual functionality you want for the buttons on the main page
    print("Button clicked!")

# Create themed main window
root = tk.Tk()
root.title("Creative Login Form")

# Create widgets
background_image = tk.PhotoImage(file="C:/Users/RAD 182/PycharmProjects/pythonProject2/img/78.png")
background_label = ttk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

new_username_label = ttk.Label(root, text="New Username:")
new_username_entry = ttk.Entry(root)

new_password_label = ttk.Label(root, text="New Password:")
new_password_entry = ttk.Entry(root, show="*")

create_account_button = ttk.Button(root, text="Create Account", command=create_account, style="success.TButton")

username_label = ttk.Label(root, text="Username:")
username_entry = ttk.Entry(root)

password_label = ttk.Label(root, text="Password:")
password_entry = ttk.Entry(root, show="*")

login_button = ttk.Button(root, text="Login", command=login, style="primary.TButton")

status_label = ttk.Label(root, text="")

# Center the login widgets horizontally and vertically
new_username_label.place(relx=0.5, rely=0.3, anchor="center")
new_username_entry.place(relx=0.5, rely=0.35, anchor="center")
new_password_label.place(relx=0.5, rely=0.4, anchor="center")
new_password_entry.place(relx=0.5, rely=0.45, anchor="center")
create_account_button.place(relx=0.5, rely=0.5, anchor="center")
username_label.place(relx=0.5, rely=0.6, anchor="center")
username_entry.place(relx=0.5, rely=0.65, anchor="center")
password_label.place(relx=0.5, rely=0.7, anchor="center")
password_entry.place(relx=0.5, rely=0.75, anchor="center")
login_button.place(relx=0.5, rely=0.8, anchor="center")
status_label.place(relx=0.5, rely=0.9, anchor="center")

# Start the Tkinter main loop
root.mainloop()

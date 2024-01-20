import tkinter as tk
import shelve

def create_account():
    username = new_username_entry.get()
    password = new_password_entry.get()

    if not username or not password:
        status_label.config(text="Please enter both username and password.")
        return

    user_data = shelve.open("user_data")
    if username in user_data:
        status_label.config(text="Username already exists. Try a different one.")
    else:
        user_data[username] = password
        status_label.config(text="Account created successfully.")
    user_data.close()

def login():
    username = username_entry.get()
    password = password_entry.get()

    user_data = shelve.open("user_data")
    stored_password = user_data.get(username, None)
    user_data.close()

    if stored_password is None:
        status_label.config(text="Invalid username. Please try again.")
    elif password == stored_password:
        status_label.config(text="Login successful.")
    else:
        status_label.config(text="Incorrect password. Please try again.")

# Create main window
root = tk.Tk()
root.title("Login Form")

# Create widgets
new_username_label = tk.Label(root, text="New Username:")
new_username_entry = tk.Entry(root)

new_password_label = tk.Label(root, text="New Password:")
new_password_entry = tk.Entry(root, show="*")

create_account_button = tk.Button(root, text="Create Account", command=create_account)

username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")

login_button = tk.Button(root, text="Login", command=login)

status_label = tk.Label(root, text="")

# Grid layout
new_username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
new_username_entry.grid(row=0, column=1, padx=10, pady=5)
new_password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
new_password_entry.grid(row=1, column=1, padx=10, pady=5)
create_account_button.grid(row=2, column=1, pady=10)

username_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
username_entry.grid(row=3, column=1, padx=10, pady=5)
password_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
password_entry.grid(row=4, column=1, padx=10, pady=5)
login_button.grid(row=5, column=1, pady=10)

status_label.grid(row=6, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
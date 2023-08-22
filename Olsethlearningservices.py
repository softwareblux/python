import os
import shutil
from tkinter import Tk, Button, Text, filedialog, Label, Entry
from tkinter import ttk
from passlib.hash import pbkdf2_sha256
import requests
import sqlite3

API_BASE_URL = "http://your-api-url.com"

# Initialize the database connection
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create a table for user registration
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """
)
conn.commit()

# Update the USERS dictionary with a custom username and password
USERS = {
    "admin": "$pbkdf2-sha256$29000$DcDcDW9LdrwflIO7Zdpa8Q$frccB46zwxKzXwhNqxGBikwESuh2ZfhrR40ziC/fG1g",
    "210804": pbkdf2_sha256.hash("Krister")
}

class CommentingApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Commenting App")

        # Calculate the center coordinates of the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 600) // 2  # Adjust the width as desired
        y = (screen_height - 400) // 2  # Adjust the height as desired

        # Set the window size and position
        self.root.geometry(f"600x400+{x}+{y}")

        # Create a Label for username
        self.username_label = Label(self.root, text="Username:")
        self.username_label.pack()

        # Create an Entry widget for username
        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        # Create a Label for password
        self.password_label = Label(self.root, text="Password:")
        self.password_label.pack()

        # Create an Entry widget for password
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        # Create a "Login" button
        self.login_button = Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

        # Create a "Register" button
        self.register_button = Button(self.root, text="Register", command=self.register)
        self.register_button.pack()

        self.comments = {}
        self.logged_in = False

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in USERS:
            hashed_password = USERS[username]
            if pbkdf2_sha256.verify(password, hashed_password):
                self.logged_in = True
                self.username_label.pack_forget()
                self.username_entry.pack_forget()
                self.password_label.pack_forget()
                self.password_entry.pack_forget()
                self.login_button.pack_forget()
                self.register_button.pack_forget()
                self.initialize_app()
                print("Login successful!")
            else:
                print("Incorrect password!")
        else:
            print("Username not found!")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            try:
                hashed_password = pbkdf2_sha256.hash(password)

                # Insert user credentials into the database
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
                conn.commit()

                print("Registration successful!")
            except sqlite3.IntegrityError:
                print("Username already exists!")
        else:
            print("Username and password are required!")

    def initialize_app(self):
        # Create a "Upload File" button
        self.upload_button = Button(self.root, text="Upload File", command=self.upload_file)
        self.upload_button.pack()

        # Create a Treeview widget to display file names
        self.treeview = ttk.Treeview(self.root, columns=("File Name",))
        self.treeview.heading("#0", text="ID")
        self.treeview.column("#0", width=50, anchor="center")
        self.treeview.heading("File Name", text="File Name")
        self.treeview.pack()

        # Create a "Download" button
        self.download_button = Button(self.root, text="Download", command=self.download_file, state="disabled")
        self.download_button.pack()

        # Create a Text widget for comments
        self.comment_text = Text(self.root, height=10, width=60)
        self.comment_text.pack()

        # Create a "Save Comment" button
        self.save_comment_button = Button(self.root, text="Save Comment", command=self.save_comment, state="disabled")
        self.save_comment_button.pack()

        # Create a "Refresh" button
        self.refresh_button = Button(self.root, text="Refresh", command=self.refresh)
        self.refresh_button.pack()

        self.populate_treeview("uploads")

    def populate_treeview(self, folder):
        self.treeview.delete(*self.treeview.get_children())
        for idx, file_name in enumerate(os.listdir(folder)):
            self.treeview.insert(parent="", index="end", iid=idx, text=idx, values=(file_name,))

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if file_path:
            self.handle_uploaded_file(file_path)

    def handle_uploaded_file(self, file_path):
        file_name = os.path.basename(file_path)
        destination_folder = "uploads"
        destination_path = os.path.join(destination_folder, file_name)
        os.makedirs(destination_folder, exist_ok=True)
        shutil.copy2(file_path, destination_path)
        self.populate_treeview(destination_folder)

    def download_file(self):
        selection = self.treeview.selection()
        if selection:
            item = self.treeview.item(selection[0])
            file_name = item["values"][0]
            file_path = os.path.join("uploads", file_name)
            if os.path.exists(file_path):
                response = requests.get(f"{API_BASE_URL}/download/{file_name}")
                if response.status_code == 200:
                    with open(file_name, "wb") as file:
                        file.write(response.content)
                    print("Download successful!")
                else:
                    print("Failed to download file.")
            else:
                print("File does not exist.")

    def save_comment(self):
        selection = self.treeview.selection()
        if selection:
            item = self.treeview.item(selection[0])
            file_name = item["values"][0]
            comment = self.comment_text.get("1.0", "end-1c")
            if file_name in self.comments:
                self.comments[file_name].append(comment)
            else:
                self.comments[file_name] = [comment]
            print("Comment saved!")

    def refresh(self):
        selection = self.treeview.selection()
        if selection:
            item = self.treeview.item(selection[0])
            file_name = item["values"][0]
            comments = self.comments.get(file_name, [])
            self.comment_text.delete("1.0", "end")
            for comment in comments:
                self.comment_text.insert("end", comment + "\n")
        else:
            self.comment_text.delete("1.0", "end")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CommentingApp()
    app.run()

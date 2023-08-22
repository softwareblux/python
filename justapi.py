# # # from tkinter import Tk, Frame, Menu, messagebox, Text, Scrollbar, Toplevel, Label, Entry, Button
# # # from tkinter import ttk
# # # import requests
# # # import json
# # # import random
# # # import string
# # # import hashlib
# # # import matplotlib.pyplot as plt


# # # API_BASE_URL = "http://10.0.0.33:5000/api"

# # # class SchoolSoftware:
# # #     def __init__(self):
# # #         self.root = Tk()
# # #         self.root.title("School Software")

# # #         # Calculate the center coordinates of the screen
# # #         screen_width = self.root.winfo_screenwidth()
# # #         screen_height = self.root.winfo_screenheight()
# # #         x = (screen_width - 800) // 2  # Adjust the width as desired
# # #         y = (screen_height - 600) // 2  # Adjust the height as desired

# # #         # Set the window size and position
# # #         self.root.geometry(f"800x600+{x}+{y}")

# # #         # Create a menu bar
# # #         menu_bar = Menu(self.root)
# # #         self.root.config(menu=menu_bar)

# # #         # Create the File menu
# # #         file_menu = Menu(menu_bar, tearoff=0)
# # #         file_menu.add_command(label="Exit", command=self.root.quit)
# # #         menu_bar.add_cascade(label="File", menu=file_menu)

# # #         # Create the Student menu
# # #         student_menu = Menu(menu_bar, tearoff=0)
# # #         student_menu.add_command(label="Add Student", command=self.add_student)
# # #         student_menu.add_command(label="View Students", command=self.view_students)
# # #         menu_bar.add_cascade(label="Students", menu=student_menu)

# # #         # Create the Reports menu
# # #         reports_menu = Menu(menu_bar, tearoff=0)
# # #         reports_menu.add_command(label="Attendance Report", command=self.generate_attendance_report)
# # #         reports_menu.add_command(label="Grade Report", command=self.generate_grade_report)
# # #         menu_bar.add_cascade(label="Reports", menu=reports_menu)

# # #         # Create a Frame to hold the Treeview and Scrollbar
# # #         frame = Frame(self.root)
# # #         frame.pack(fill="both", expand=True)

# # #         # Create a Treeview widget to display the API content
# # #         self.treeview = ttk.Treeview(frame, columns=("Student ID", "Test Name", "Score"))
# # #         self.treeview.heading("Student ID", text="Student ID")
# # #         self.treeview.heading("Test Name", text="Test Name")
# # #         self.treeview.heading("Score", text="Score")
# # #         self.treeview.pack(side="left", fill="both", expand=True)

# # #         # Create a Scrollbar for the Treeview
# # #         tree_scrollbar = Scrollbar(frame, orient="vertical")
# # #         tree_scrollbar.pack(side="right", fill="y")

# # #         # Configure the Scrollbar to work with the Treeview
# # #         self.treeview.configure(yscrollcommand=tree_scrollbar.set)
# # #         tree_scrollbar.configure(command=self.treeview.yview)

# # #         # Create a new button to open the student names page
# # #         self.names_button = ttk.Button(self.root, text="View Student Names", command=self.open_login_window)
# # #         self.names_button.pack()

# # #         self.populate_treeview()

# # #     def add_student(self):
# # #         # Implement the functionality to add a student
# # #         messagebox.showinfo("Add Student", "Add Student functionality will be implemented here.")

# # #     def view_students(self):
# # #         # Implement the functionality to view students
# # #         messagebox.showinfo("View Students", "View Students functionality will be implemented here.")

# # #     def generate_attendance_report(self):
# # #         # Implement the functionality to generate attendance report
# # #         messagebox.showinfo("Attendance Report", "Attendance Report functionality will be implemented here.")

# # #     def generate_grade_report(self):
# # #         # Implement thefunctionality to generate grade report
# # #         messagebox.showinfo("Grade Report", "Grade Report functionality will be implemented here.")

# # #     def populate_treeview(self):
# # #         # Send request to the API to get the student data
# # #         response = requests.get(API_BASE_URL + "/students")
# # #         if response.status_code == 200:
# # #             try:
# # #                 student_data = response.json()
# # #                 self.treeview.delete(*self.treeview.get_children())
# # #                 for student in student_data:
# # #                     student_name = student["name"]
# # #                     code = self.generate_code(student_name)

# # #                     response = requests.get(API_BASE_URL + f"/students/{student['id']}/tests")
# # #                     if response.status_code == 200:
# # #                         test_data = response.json()
# # #                         for test in test_data:
# # #                             test_name = test["name"]
# # #                             test_score = test["score"]
# # #                             item_id = f"test_{student['id']}_{test_name}"  # Unique item ID for tests
# # #                             self.treeview.insert(parent="", index="end", iid=item_id, text="", values=(code, test_name, test_score))
# # #             except json.decoder.JSONDecodeError:
# # #                 print("Invalid JSON data received.")
# # #                 self.treeview.delete(*self.treeview.get_children())
# # #                 self.treeview.insert(parent="", index="end", iid="no_data", text="No data available.")
# # #         else:
# # #             print("Failed to retrieve student data.")

# # #     def generate_code(self, student_name):
# # #         # Generate a unique code for the student based on their name
# # #         # Using hashlib and SHA256 for consistent hash value
# # #         hash_object = hashlib.sha256(student_name.encode())
# # #         code = hash_object.hexdigest()[:6]  # Extract the first 6 characters
# # #         return code

# # #     def open_login_window(self):
# # #         # Create a login window
# # #         login_window = Toplevel(self.root)
# # #         login_window.title("Login")

# # #         # Create labels and entries for username and password
# # #         username_label = Label(login_window, text="Username:")
# # #         username_label.pack()
# # #         username_entry = Entry(login_window)
# # #         username_entry.pack()

# # #         password_label = Label(login_window, text="Password:")
# # #         password_label.pack()
# # #         password_entry = Entry(login_window, show="*")
# # #         password_entry.pack()

# # #         # Create a login button
# # #         login_button = Button(login_window, text="Login", command=lambda: self.login(login_window, username_entry.get(), password_entry.get()))
# # #         login_button.pack()

# # #     def login(self, login_window, username, password):
# # #         # Perform login validation
# # #         if username == "admin" and password == "Krister":
# # #             login_window.destroy()
# # #             self.view_student_names()
# # #         else:
# # #             messagebox.showerror("Login Failed", "Invalid username or password.")

# # #     def view_student_names(self):
# # #         # Open a new window to display student names and codes
# # #         names_window = Toplevel(self.root)
# # #         names_window.title("Student Names and Codes")

# # #         # Create a Text widget to display the student names and codes
# # #         text_widget = Text(names_window)
# # #         text_widget.pack()

# # #         # Send request to the API to get the student data
# # #         response = requests.get(API_BASE_URL + "/students")
# # #         if response.status_code == 200:
# # #             try:
# # #                 student_data = response.json()
# # #                 student_names = []
# # #                 for student in student_data:
# # #                     name = student["name"]
# # #                     code = self.generate_code(name)
# # #                     student_names.append(f"{name} = {code}")
# # #                 names_text = "\n".join(student_names)
# # #                 text_widget.insert("1.0", names_text)
# # #             except json.decoder.JSONDecodeError:
# # #                 text_widget.insert("1.0", "Invalid JSON data received.")
# # #         else:
# # #             text_widget.insert("1.0", "Failed toretrieve student data.")

# # #     def run(self):
# # #         self.root.mainloop()


# # # if __name__ == "__main__":
# # #     app = SchoolSoftware()
# # #     app.run()



# from tkinter import Tk, Frame, Menu, messagebox, Scrollbar, Toplevel, Label, Entry, Button
# from tkinter import ttk
# import requests
# import json

# # Replace these with the appropriate URLs for your API endpoints
# API_BASE_URL = "http://127.0.0.1:5000/insert"
# API_BASE_URL_GET = "http://127.0.0.1:5000/query"


# class SchoolSoftware:
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("School Software")

#         # Calculate the center coordinates of the screen
#         screen_width = self.root.winfo_screenwidth()
#         screen_height = self.root.winfo_screenheight()
#         x = (screen_width - 800) // 2  # Adjust the width as desired
#         y = (screen_height - 600) // 2  # Adjust the height as desired

#         # Set the window size and position
#         self.root.geometry(f"800x600+{x}+{y}")

#         # Create a menu bar
#         menu_bar = Menu(self.root)
#         self.root.config(menu=menu_bar)

#         # Create the File menu
#         file_menu = Menu(menu_bar, tearoff=0)
#         file_menu.add_command(label="Exit", command=self.root.quit)
#         menu_bar.add_cascade(label="File", menu=file_menu)

#         # Create the Student menu
#         student_menu = Menu(menu_bar, tearoff=0)
#         student_menu.add_command(label="Add Student", command=self.add_student)
#         student_menu.add_command(label="View Students", command=self.show_students_window)
#         menu_bar.add_cascade(label="Students", menu=student_menu)

#         # Create the Reports menu
#         reports_menu = Menu(menu_bar, tearoff=0)
#         reports_menu.add_command(label="Attendance Report", command=self.generate_attendance_report)
#         reports_menu.add_command(label="Grade Report", command=self.generate_grade_report)
#         menu_bar.add_cascade(label="Reports", menu=reports_menu)

#         self.students_window = None  # Reference to the "View Students" window
#         self.students_treeview = None  # Reference to the Treeview in "View Students" window

#     def show_students_window(self):
#         if self.students_window is None or not self.students_window.winfo_exists():
#             self.students_window = Toplevel(self.root)
#             self.students_window.title("View Students")
#             self.students_window.protocol("WM_DELETE_WINDOW", self.on_students_window_close)  # Handle window close event

#             # Create a Frame to hold the Treeview and Scrollbar
#             frame = Frame(self.students_window)
#             frame.pack(fill="both", expand=True)

#             # Create a Treeview widget to display the student data
#             self.students_treeview = ttk.Treeview(frame, columns=("Student ID", "Name", "Email", "From Date"))
#             self.students_treeview.heading("Student ID", text="Student ID")
#             self.students_treeview.heading("Name", text="Name")
#             self.students_treeview.heading("Email", text="Email")
#             self.students_treeview.heading("From Date", text="From Date")
#             self.students_treeview.bind("<Double-1>", self.show_student_info)  # Bind double-click event to show student info
#             self.students_treeview.pack(side="left", fill="both", expand=True)

#             # Create a Scrollbar for the Treeview
#             tree_scrollbar = Scrollbar(frame, orient="vertical")
#             tree_scrollbar.pack(side="right", fill="y")

#             # Configure the Scrollbar to work with the Treeview
#             self.students_treeview.configure(yscrollcommand=tree_scrollbar.set)
#             tree_scrollbar.configure(command=self.students_treeview.yview)

#         self.populate_treeview()

#     def on_students_window_close(self):
#         self.students_window.destroy()
#         self.students_window = None
#         self.students_treeview = None

#     def add_student(self):
#         # Open a new window to add a student
#         add_window = Toplevel(self.root)
#         add_window.title("Add Student")

#         # Create labels and entries for student details
#         id_label = Label(add_window, text="Student id:")
#         id_label.pack()
#         id_entry = Entry(add_window)
#         id_entry.pack()

#         name_label = Label(add_window, text="Name:")
#         name_label.pack()
#         name_entry = Entry(add_window)
#         name_entry.pack()

#         email_label = Label(add_window, text="Email:")
#         email_label.pack()
#         email_entry = Entry(add_window)
#         email_entry.pack()

#         from_date_label = Label(add_window, text="From Date:")
#         from_date_label.pack()
#         from_date_entry = Entry(add_window)
#         from_date_entry.pack()

#         def save_student():
#             # Extract the values from the entries
#             id = id_entry.get()
#             name = name_entry.get()
#             email = email_entry.get()
#             from_date = from_date_entry.get()  # Get the value of the "from_date" entry

#             # Create the JSON payload
#             new_student = {
#                 "id": id,
#                 "name": name,
#                 "email": email,
#                 "from_date": from_date  # Include "from_date" in the JSON payload
#             }

#             # Send request to the API to add the student
#             response = requests.post(API_BASE_URL, json=new_student)
#             if response.status_code == 200:
#                 messagebox.showinfo("Success", "Student added successfully.")
#                 add_window.destroy()
#                 self.populate_treeview()
#             else:
#                 messagebox.showerror("Error", "Failed to add student API.")

#         save_button = Button(add_window, text="Save", command=save_student)
#         save_button.pack()

#     def populate_treeview(self):
#         if self.students_treeview is not None and self.students_treeview.winfo_exists():
#             self.students_treeview.delete(*self.students_treeview.get_children())

#         # Send request to the API to get the student data
#         response = requests.get(API_BASE_URL_GET)
#         if response.status_code == 200:
#             try:
#                 student_data = response.json()
#                 for student in student_data:
#                     student_id = student["id"]
#                     name = student["name"]
#                     email = student.get("email", "")  # Use the get method with a default value of empty string
#                     from_date = student.get("from_date", "")  # Get the "from_date" from the response

#                     # Insert the data into the Treeview
#                     self.students_treeview.insert(parent="", index="end", values=(student_id, name, email, from_date))

#             except json.decoder.JSONDecodeError:
#                 messagebox.showerror("Error", "Invalid JSON data received.")
#         else:
#             messagebox.showerror("Error", "Failed to retrieve student data.")

#     def generate_attendance_report(self):
#         # Implement the functionality to generate attendance report
#         messagebox.showinfo("Attendance Report", "Attendance Report functionality will be implemented here.")

#     def generate_grade_report(self):
#         # Implement the functionality to generate grade report
#         messagebox.showinfo("Grade Report", "Grade Report functionality will be implemented here.")

#     def show_student_info(self, event):
#         # Get the selected item in the Treeview
#         item = self.students_treeview.focus()
#         if item:
#             student_id = self.students_treeview.item(item, "values")[0]  # Get the student ID from the Treeview
#             student_info = self.students_treeview.item(item, "values")[1:]  # Get the rest of the student info
#             messagebox.showinfo("Student Information", f"Student ID: {student_id}\nName: {student_info[0]}\nEmail: {student_info[1]}\nFrom Date: {student_info[2]}")

#     def run(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     app = SchoolSoftware()
#     app.run()




from tkinter import Tk, Frame, Menu, messagebox, Scrollbar, Toplevel, Label, Entry, Button
from tkinter import ttk
import requests
import json

# Sample username and password (you should use a secure authentication system in practice)
USERNAME = "admin"
PASSWORD = "password"

# Define the API endpoints for adding a student and retrieving student data
API_BASE_URL = "http://127.0.0.1:5000/insert"
API_BASE_URL_GET = "http://127.0.0.1:5000/query"


class SchoolSoftware:
    def __init__(self):
        self.root = Tk()
        self.root.title("School Software")

        # Calculate the center coordinates of the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 800) // 2  # Adjust the width as desired
        y = (screen_height - 600) // 2  # Adjust the height as desired

        # Set the window size and position
        self.root.geometry(f"800x600+{x}+{y}")

        # Create a menu bar
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Create the File menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Create the Student menu
        student_menu = Menu(menu_bar, tearoff=0)
        student_menu.add_command(label="Add Student", command=self.add_student)
        student_menu.add_command(label="View Students", command=self.show_login_window)
        menu_bar.add_cascade(label="Students", menu=student_menu)

        # Create the Reports menu
        reports_menu = Menu(menu_bar, tearoff=0)
        reports_menu.add_command(label="Attendance Report", command=self.generate_attendance_report)
        reports_menu.add_command(label="Grade Report", command=self.generate_grade_report)
        menu_bar.add_cascade(label="Reports", menu=reports_menu)

        self.students_window = None  # Reference to the "View Students" window
        self.students_treeview = None  # Reference to the Treeview in "View Students" window

    def show_login_window(self):
        login_window = Toplevel(self.root)
        login_window.title("Login")

        Label(login_window, text="Username:").pack()
        username_entry = Entry(login_window)
        username_entry.pack()

        Label(login_window, text="Password:").pack()
        password_entry = Entry(login_window, show="*")
        password_entry.pack()

        def login():
            username = username_entry.get()
            password = password_entry.get()

            if username == USERNAME and password == PASSWORD:
                login_window.destroy()
                self.show_students_window()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        login_button = Button(login_window, text="Login", command=login)
        login_button.pack()

    def show_students_window(self):
        if self.students_window is None or not self.students_window.winfo_exists():
            self.students_window = Toplevel(self.root)
            self.students_window.title("View Students")
            self.students_window.protocol("WM_DELETE_WINDOW", self.on_students_window_close)  # Handle window close event

            # Create a Frame to hold the Treeview and Scrollbar
            frame = Frame(self.students_window)
            frame.pack(fill="both", expand=True)

            # Create a Treeview widget to display the student data
            self.students_treeview = ttk.Treeview(frame, columns=("Student ID", "Name", "Email", "From Date"))
            self.students_treeview.heading("Student ID", text="Student ID")
            self.students_treeview.heading("Name", text="Name")
            self.students_treeview.heading("Email", text="Email")
            self.students_treeview.heading("From Date", text="From Date")
            self.students_treeview.bind("<Double-1>", self.show_student_info)  # Bind double-click event to show student info
            self.students_treeview.pack(side="left", fill="both", expand=True)

            # Create a Scrollbar for the Treeview
            tree_scrollbar = Scrollbar(frame, orient="vertical")
            tree_scrollbar.pack(side="right", fill="y")

            # Configure the Scrollbar to work with the Treeview
            self.students_treeview.configure(yscrollcommand=tree_scrollbar.set)
            tree_scrollbar.configure(command=self.students_treeview.yview)

            # Populate the Treeview with student data
            self.populate_treeview()

    def on_students_window_close(self):
        self.students_window.destroy()
        self.students_window = None
        self.students_treeview = None

    def add_student(self):
        # Open a new window to add a student
        add_window = Toplevel(self.root)
        add_window.title("Add Student")

        Label(add_window, text="Student ID:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = Entry(add_window)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        Label(add_window, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        name_entry = Entry(add_window)
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        Label(add_window, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        email_entry = Entry(add_window)
        email_entry.grid(row=2, column=1, padx=5, pady=5)

        def save_student():
            # Extract the values from the entries
            student_id = id_entry.get()
            name = name_entry.get()
            email = email_entry.get()

            # Create the JSON payload
            new_student = {
                "id": student_id,
                "name": name,
                "email": email
            }

            # Send request to the API to add the student
            response = requests.post(API_BASE_URL, json=new_student)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully.")
                add_window.destroy()
                self.populate_treeview()  # Update the treeview after adding a new student
            else:
                messagebox.showerror("Error", "Failed to add student to the API.")

        save_button = Button(add_window, text="Save", command=save_student)
        save_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        

    def populate_treeview(self):
        if self.students_treeview is not None:
            self.students_treeview.delete(*self.students_treeview.get_children())

            # Send request to the API to get the student data
            response = requests.get(API_BASE_URL_GET)
            if response.status_code == 200:
                try:
                    student_data = response.json()
                    for student in student_data:
                        student_id = student["id"]
                        name = student["name"]
                        email = student.get("email", "")  # Use the get method with a default value of empty string
                        from_date = student.get("from_date", "")  # Get the "from_date" from the response

                        # Insert the data into the Treeview
                        self.students_treeview.insert(parent="", index="end", values=(student_id, name, email, from_date))

                except json.decoder.JSONDecodeError:
                    messagebox.showerror("Error", "Invalid JSON data received.")
            else:
                messagebox.showerror("Error", "Failed to retrieve student data.")

    def generate_attendance_report(self):
        # Implement the functionality to generate attendance report
        messagebox.showinfo("Attendance Report", "Attendance Report functionality will be implemented here.")

    def generate_grade_report(self):
        # Implement the functionality to generate grade report
        messagebox.showinfo("Grade Report", "Grade Report functionality will be implemented here.")

    def show_student_info(self, event):
        # Get the selected item in the Treeview
        item = self.students_treeview.focus()
        if item:
            student_id = self.students_treeview.item(item, "values")[0]  # Get the student ID from the Treeview
            student_info = self.students_treeview.item(item, "values")[1:]  # Get the rest of the student info
            messagebox.showinfo("Student Information", f"Student ID: {student_id}\nName: {student_info[0]}\nEmail: {student_info[1]}\nFrom Date: {student_info[2]}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SchoolSoftware()
    app.run()



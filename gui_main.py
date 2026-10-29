import tkinter as tk

from database import Database
from tkinter import messagebox
from enrolment_window import open_enrolment_window
from validation import validate_email

root = tk.Tk()
root.title("University Login")
root.geometry("400x300")
database = Database()

def login():
    email = email_entry.get()
    password = password_entry.get()
    if email.strip() =="" and password.strip() == "":
        messagebox.showerror("Login Error", "Email and passoword cannot be empty.")
        return
    if email.strip() == "":
        messagebox.showerror("Login Error", "Email cannot be empty.")
        return
    if password.strip() == "":
        messagebox.showerror("Login Error", "Password cannot be empty.")
        return
    if not validate_email(email):
        messagebox.showerror("Login Error", "Invalid email format.")
        return
    students = database.read_students()
    for student in students:
        if student.email == email and student.password == password:
            messagebox.showinfo("Login", "Login successful")
            open_enrolment_window(student)
            return
    messagebox.showerror("Login Error", "Invalid email or password.")



title_label = tk.Label(root, text="Student Login", font=("Arial", 18))
title_label.pack(pady=20)

email_label = tk.Label(root, text="Email:")
email_label.pack()

email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)


login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)
root.mainloop()
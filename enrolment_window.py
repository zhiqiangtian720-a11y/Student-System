import tkinter as tk
from tkinter import messagebox
from subject import Subject
from database import Database
from subject_window import open_subject_window

database = Database()

def save_student(updated_student):
    students = database.read_students()

    for i in range(len(students)):
        if students[i].student_id == updated_student.student_id:
            students[i] = updated_student
            break

    database.write_students(students)

def open_enrolment_window(student):
    window = tk.Toplevel()

    window.title("Subject Enrolment")
    window.geometry("500x400")
    
    def enrol_subject():
        if len(student.subjects) >= 4:
            messagebox.showerror(
                "Enrolment Error",
                "You cannot enrol in more than 4 subjects."
            )
            return

        subject = Subject()

        student.enrol_subject(subject)

        save_student(student)

        messagebox.showinfo(
            "Enrolment",
            "Subject enrolled successfully."
        )
    title_label = tk.Label(
        window,
        text="Subject Enrolment",
        font=("Arial", 18)
    )
    title_label.pack(pady=20)
    
    welcome_label = tk.Label(
        window,
        text="Welcome " + student.name
    )
    welcome_label.pack(pady=10)
    
    enrol_button = tk.Button(
        window,
        text="Enrol Subject",
        command=enrol_subject
    )
    enrol_button.pack(pady=10)
    
    view_button = tk.Button(
        window,
        text="View Subjects",
        command=lambda: open_subject_window(student)
    )
    view_button.pack(pady=10)
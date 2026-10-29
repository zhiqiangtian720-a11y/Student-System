import tkinter as tk


def open_subject_window(student):
    window = tk.Toplevel()

    window.title("Subjects")
    window.geometry("500x400")

    title_label = tk.Label(
        window,
        text="My Subjects",
        font=("Arial", 18)
    )
    title_label.pack(pady=20)

    if len(student.subjects) == 0:
        no_subject_label = tk.Label(
            window,
            text="No subjects enrolled."
        )
        no_subject_label.pack(pady=10)
        return

    for subject in student.subjects:
        subject_label = tk.Label(
            window,
            text=(
                "Subject ID: " + str(subject.subject_id)
                + " | Mark: " + str(subject.mark)
                + " | Grade: " + subject.grade
            )
        )
        subject_label.pack(pady=5)

    average = student.calculate_average_mark()

    average_label = tk.Label(
        window,
        text="Average Mark: " + str(round(average, 2))
    )
    average_label.pack(pady=20)
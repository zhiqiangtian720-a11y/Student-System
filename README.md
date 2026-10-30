# Student System

This project is a University Student System developed in Python.

## Features

### CLI Application
- Student registration
- Student login
- Email and password validation
- Subject enrolment
- Remove subject
- View subject marks and grades
- Change password
- Admin functions
- Student data management

### GUI Application
- Student login
- Subject enrolment
- View enrolled subjects
- View marks and grades
- Error handling for invalid input

## Data Storage

Student information is stored in:

`students.data`

The CLI and GUI applications use the same student data file.

## How to Run

### CLI Version

Run:

`python main.py`

### GUI Version

Run:

`python gui_main.py`

## Main Files

- `main.py` – starts the CLI application
- `gui_main.py` – starts the GUI application
- `student_controller.py` – handles student registration and login
- `subject_controller.py` – handles subject enrolment functions
- `admin_controller.py` – handles admin functions
- `student.py` – Student class
- `subject.py` – Subject class
- `database.py` – handles reading and writing student data
- login_window.py – displays the GUI login window
- enrolment_window.py – handles GUI subject enrolment
- subject_window.py – displays enrolled subjects, marks and grades
- university_controller.py – controls the main University menu

## Technology

- Python
- Tkinter
- Object-Oriented Programming (OOP)

from subject import Subject
from database import Database
from validation import validate_password

class SubjectController:
    def __init__(self):
        self.database = Database()

    def subject_menu(self,student):
        while True:
            print("\nSubject Enrolment System")
            print("(c) change password")
            print("(e) enrol")
            print("(r) remove")
            print("(s) show")
            print("(x) exit")
            
            choice = input("Choose an option: ").lower()

            if choice == "e":
                self.enrol_subject(student)
            elif choice == "r":
                self.remove_subject(student)
            elif choice == "s":
                self.show_subjects(student)
            elif choice == "c":
                self.change_password(student)
            elif choice == "x":
                print("Exiting Subject Enrolment System.")
                break
            else:
                print("Invalid option. Please try again.")

    def enrol_subject(self,student):
        new_subject = Subject()
        if student.enrol_subject(new_subject):
            self.save_student(student)
            print("Enrolment successful")
            print(new_subject)
            average = student.calculate_average_mark()
        else:
            print("Student are allowed to enrol in 4 subjects only")

    def save_student(self, update_student):
        students = self.database.read_students()
        for i in range(len(students)):
            if students[i].student_id == update_student.student_id:
                students[i] = update_student
                break
        self.database.write_students(students)

    def show_subjects(self, student):
        if len(student.subjects) == 0:
            print("No enrolled subjects.")
            return
        print("Enrolled Subjects:")
        for subject in student.subjects:
            print(subject)
        average = student.calculate_average_mark()
        print("Average mark: ", round(average, 2))

    def remove_subject(self, student):
        while True:
            if len(student.subjects) == 0:
                print("No suvject to remove.")
                return
            self.show_subjects(student)
            subject_id = input("Enter subject ID to remove (x to cancel): ")
            if subject_id.lower() == "x":
                return
            if not subject_id.isdigit() or len(subject_id) != 3:
                print("Invalid subject ID.")
                continue
            if student.remove_subject(subject_id):
                self.save_student(student)
                print("Subject removed successfully")
                return
            else:
                print("Subject not found")

    def change_password(self, student):
        while True:
            new_password = input("Enter new password (x to cancel): ")
            if new_password.lower() == "x":
                return
            if new_password.strip() == "":
                print("Password cannot be empty.")
                continue
            if not validate_password(new_password):
                print("Invalid password format. Please try again.")
                continue
            student.change_password(new_password)
            self.save_student(student)
            print("Password changed successfully.")
            return

from database import Database

class AdminController:
    def __init__(self):
        self.database = Database()

    def admin_menu(self):
        while True:
            print("\nAdmin System")
            print("(c) clear database")
            print("(g) group students")
            print("(p) partition PASS / FAIL")
            print("(r) remove student")
            print("(s) show students")
            print("(x) exit")
            choice = input("Choose an option: ").lower()
            if choice == "s":
                self.show_students()
            elif choice == "p":
                self.partiton_student()
            elif choice == "g":
                self.group_students()
            elif choice == "r":
                self.remove_student()
            elif choice == "c":
                self.clear_database()
            elif choice == "x":
                print("Exiting Admin System.")
                break
            else:
                print("Invalid option. Please try again")

    def show_students(self):
        students = self.database.read_students()
        if len(students) == 0:
            print("No students found.")
            return
        print("Students:")
        for student in students:
            print(
                "Student ID:", student.student_id,
                "| Name:", student.name,
                "| Email:", student.email
            )

    def partiton_student(self):
        students = self.database.read_students()
        if len(students) == 0:
            print("No students found.")
            return
        pass_student = []
        fail_student = []
        for student in students:
            if len(student.subjects) < 4:
                print(student.name, "does not have 4 subjects yet.")
                continue
            if student.is_pass():
                pass_student.append(student)
            else:
                fail_student.append(student)
        print("\nPASS Students:")
        for student in pass_student:
            print(
                "Student ID:", student.student_id,
                "| Name:", student.name,
                "| Grade:" ,student.calculate_grade(),
                "| Average:", round(student.calculate_average_mark(), 2)
                )
        print("\nFAIL Students:")
        for student in fail_student:
            print(
                "Student ID:", student.student_id,
                "| Name:", student.name,
                "| Grade:" ,student.calculate_grade(),
                "| Average:", round(student.calculate_average_mark(), 2)
            )

    def group_students(self):
        students = self.database.read_students()
        if len(students) == 0:
            print("No students found.")
            return
        groups = {
            "HD": [],
            "D": [],
            "C": [],
            "P": [],
            "Z": [],
        }
        for student in students:
            if len(student.subjects) == 0:
                print(student.name, "has no enrolled subjects.")
                continue
            grade = student.calculate_grade()
            groups[grade].append(student)
        for grade in groups:
            print("\nGrade", grade)
            for student in groups[grade]:
                print(
                    "Student ID:", student.student_id,
                    "| Name:", student.name,
                    "| Grade:" ,student.calculate_grade(),
                    "| Average:", round(student.calculate_average_mark(), 2)
                )

    def remove_student(self):
        students = self.database.read_students()
        if len(students) == 0:
            print("No students found.")
            return
        student_id = input("Enter student ID to remove: ")
        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                self.database.write_students(students)
                print("Student removed successfully.")
                return
        print("Student not found.")

    def clear_database(self):
        confirm = input("Are you sure you want to clear all student data? (y/n): ")
        if confirm == "y":
            self.database.clear_students()
            print("Database cleared successfully.")
        else:
            print("Clear database cancelled")
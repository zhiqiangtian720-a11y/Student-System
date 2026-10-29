from student_controller import StudentController
from admin_controller import AdminController

class UniversityController:
    def __init__(self):
        self.student_controller = StudentController()
        self.admin_controller = AdminController()

    def university_menu(self):
        while True:
            print("\nUniversity System")
            print("(A) Admin")
            print("(S) Student")
            print("(X) Exit")
            choice = input("Choose an option: ").lower()
            if choice == "a":
                self.admin_controller.admin_menu()
            elif choice == "s":
                self.student_controller.student_menu()
            elif choice == "x":
                print("Exiting University System.")
                break
            else:
                print("Invalid option. Please try again.")
class Student:
    def __init__(self, student_id, name, email, password):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    def change_password(self, new_password):
        self.password = new_password

    def enrol_subject(self, subject):
        if len(self.subjects) < 4:
            self.subjects.append(subject)
            return True
        else:
            return False

    def remove_subject(self, subject_id):
        for subject in self.subjects:
            if subject.subject_id == subject_id:
                self.subjects.remove(subject)
                return True
        return False

    def show_subjects(self):
        for subject in self.subjects:
            print(subject)

    def calculate_average_mark(self):
        if len(self.subjects) == 0:
            return 0
        total_mark = 0 
        for subject in self.subjects:
            total_mark += subject.mark
        return total_mark / len(self.subjects)
    
    def is_pass(self):
        if len(self.subjects) < 4:
            return False
        return self.calculate_average_mark() >= 50

    def calculate_grade(self):
        average = self.calculate_average_mark()
        if average >= 85:
            return "HD"
        elif average >= 75:
            return "D"
        elif average >= 65:
            return "C"
        elif average >= 50:
            return "P"
        else:
            return "Z"
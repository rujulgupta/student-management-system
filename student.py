class Student:
    student_count = 0
    def __init__(self, roll_number, name, marks):

        
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

        Student.student_count += 1

    def calculate_grade(self):

        if self.marks >= 90:
            return "A+"

        elif self.marks >= 80:
            return "A"

        elif self.marks >= 70:
            return "B"

        elif self.marks >= 60:
            return "C"

        elif self.marks >= 40:
            return "D"

        else:
            return "Fail"

    def display_details(self):

        print("---------------------------------")
        print(f"Roll No : {self.roll_number}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks:g}")
        print(f"Grade   : {self.calculate_grade()}")
        print("---------------------------------")

    @classmethod
    def get_student_count(cls):

        return cls.student_counts
    @staticmethod
    def validate_marks(marks):

        return 0 <= marks <= 100
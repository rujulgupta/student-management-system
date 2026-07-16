from student import Student
class StudentManagementSystem:

    def __init__(self):
        self.students = []

    def add_student(self):
        print("\n--- Add Student ---")

        roll_number = input("Enter Roll Number: ").strip()

        for student in self.students:
            if student.roll_number == roll_number:
                print("Roll Number already exists.")
                return

        name = input("Enter Student Name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        try:
            marks = float(input("Enter Marks: "))
            if not Student.validate_marks(marks):
                print("Marks must be between 0 and 100.")
                return

        except ValueError:
            print("Invalid input. Marks must be a number.")
            return
        new_student = Student(roll_number, name, marks)

        
        self.students.append(new_student)

        print("Student Added Successfully")
    def view_students(self):
        print("\n--- Student Records ---")

        if not self.students:
            print("No Student Records Found")
            return

        for student in self.students:
            student.display_details()

        print(f"\nTotal Students: {Student.get_student_count()}")

    def search_student(self):
        print("\n--- Search Student ---")

        roll_number = input("Enter Roll Number: ").strip()

        student = self.find_student(roll_number)

        if student:
            print("\nStudent Found")
            student.display_details()
        else:
            print("Student Not Found")
    def update_marks(self):
        print("\n--- Update Marks ---")

        roll_number = input("Enter Roll Number: ").strip()

        student = self.find_student(roll_number)

        if student is None:
            print("Student Not Found")
            return

        try:
            new_marks = float(input("Enter New Marks: "))

            if not Student.validate_marks(new_marks):
                print("Marks must be between 0 and 100.")
                return

        except ValueError:
            print("Invalid input. Marks must be a number.")
            return

        student.marks = new_marks

        print("Marks Updated Successfully")

    def delete_student(self):
        print("\n--- Delete Student ---")

        roll_number = input("Enter Roll Number: ").strip()

        student = self.find_student(roll_number)

        if student:
            self.students.remove(student)

            Student.student_count -= 1

            print("Student Deleted Successfully")
        else:
            print("Student Not Found")
    def show_topper(self):
        print("\n--- Class Topper ---")

        if not self.students:
            print("No Student Records Found")
            return

        topper = self.students[0]

        for student in self.students:
            if student.marks > topper.marks:
                topper = student

        print("Topper Details")
        topper.display_details()

    def find_student(self, roll_number):

        for student in self.students:
            if student.roll_number == roll_number:
                return student

        return None


def display_menu():
    print("\n==============================")
    print("  Student Management System")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

def main():

    system = StudentManagementSystem()

    while True:

        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            system.add_student()

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            system.search_student()

        elif choice == "4":
            system.update_marks()

        elif choice == "5":
            system.delete_student()

        elif choice == "6":
            system.show_topper()

        elif choice == "7":
            print("\nThank you for using the Student Management System.")
            print("Program Exited Successfully")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
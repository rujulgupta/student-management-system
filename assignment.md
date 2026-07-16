Mini Project Assignment

Student Management System (CLI Based)

Background :

Programming Pathshala has recently started a new batch of students. Currently, all student records are maintained manually, making it difficult to search, update, and manage information.

As a Python Developer, your task is to build a Student Management System using Object-Oriented Programming (OOP) concepts. The application should run entirely in the terminal (CLI) and should be menu-driven.

Your goal is to design the application in a clean, modular, and reusable way by applying everything you've learned in Python and OOP.

Objective

Develop a command-line application that allows an administrator to manage student records.

Each student should have:

Roll Number (Unique)

Name

Marks

Functional Requirements

Your application should support the following operations:

1. Add Student

Allow the user to enter

Roll Number

Name

Marks

Validation:

Roll Number must be unique.

Marks should be between 0 and 100.

2. View All Students

Display all student records in a well-formatted manner.

Example:

---------------------------------

Roll No : 101

Name : Rahul

Marks : 92

Grade : A+

---------------------------------

3. Search Student

Search a student using Roll Number.

If found, display complete details.

Otherwise: Student Not Found

4. Update Marks

Allow updating marks using Roll Number.

After updating, display ---- Marks Updated Successfully

5. Delete Student

Delete a student using Roll Number.

Display : Student Deleted Successfully

(if found)

Otherwise : Student Not Found

6. Display Topper

Show the student with the highest marks

7. Exit

Terminate the application.

Grade Criteria

Calculate grade based on marks.

| Marks | Grade |

| -------- | ----- |

| 90–100 | A+ |

| 80–89 | A |

| 70–79 | B |

| 60–69 | C |

| 40–59 | D |

| Below 40 | Fail |

Menu
==============================

Student Management System

==============================

1. Add Student

2. View Students

3. Search Student

4. Update Marks

5. Delete Student

6. Show Topper

7. Exit

Enter your choice:

Technical Requirements :

Students must use the following concepts:

Classes & Objects

Constructors (__init__)

Instance Variables

Instance Methods

Class Variables

@classmethod

@staticmethod

Lists of Objects

Loops

Conditional Statements

Functions

if __name__ == "__main__"

Constraints :

Do not use dictionaries to store student data.

Every student must be an object.

Store all student objects inside a list.

The program should continue running until the user selects Exit.

Write clean, modular, and readable code.

SUBMISSION GUIDELINES

Repository Name : student-management-system-yourname

Repo Structure:

student-management-system/

│

├── main.py

├── student.py

├── README.md

├── .gitignore

└── screenshots/

├── menu.png

├── add_student.png

└── topper.png

&others

Google form for taking GitHub links : https://forms.gle/yMrFgK6rTzyVQ8zi7
class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.major = ""
        self.courses = ""
        self.gpa = 0.0
    def add_stu(self):
        self.id = input("Enter Student ID: ")
        self.name = input("Enter Student Name: ")
        self.major = input("Enter Major: ")
        self.courses = input("Enter Courses: ")
        self.gpa = float(input("Enter GPA: "))
    def display_stu(self):
        print("Student ID:", self.id)
        print("Name:", self.name)
        print("Major:", self.major)
        print("Courses:", self.courses)
        print("GPA:", self.gpa)
class Faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.courses_taught = ""
    def add_fac(self):
        self.id = input("Enter Faculty ID: ")
        self.name = input("Enter Faculty Name: ")
        self.department = input("Enter Department: ")
        self.courses_taught = input("Enter Courses: ")
    def display_fac(self):
        print("Faculty ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Courses taught:", self.courses_taught)


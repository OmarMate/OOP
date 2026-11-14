import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="StudentDB"
)
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        StudentID INT PRIMARY KEY,
        Name VARCHAR(50),
        Major VARCHAR(50),
        Courses VARCHAR(100),
        GPA FLOAT
    )
""")
print("Student table created successfully!")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Faculty (
        FacultyID INT PRIMARY KEY,
        Name VARCHAR(50),
        Department VARCHAR(50),
        CoursesTaught VARCHAR(100)
    )
""")
print("Faculty table created successfully!")

class Student_Master:
    def __init__(self, id, name, major, courses, cgpa):
        self.id = id
        self.name = name
        self.major = major
        self.courses = courses
        self.cgpa = cgpa

class Faculty_Master:
    def __init__(self, id, name, department, courses_taught):
        self.id = id
        self.name = name
        self.department = department
        self.courses_taught = courses_taught

student_objects = []
faculty_objects = []

def insert_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    major = input("Enter Major: ")
    courses = input("Enter Courses: ")
    gpa = float(input("Enter GPA: "))
    sql = "INSERT INTO Student VALUES (%s, %s, %s, %s, %s)"
    values = (sid, name, major, courses, gpa)
    cursor.execute(sql, values)
    db.commit()
    print("Record inserted successfully!")
def display_student():
    cursor.execute("SELECT * FROM Student")
    for row in cursor.fetchall():
        print(row)
def update_stu():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    major = input("Enter Major: ")
    courses = input("Enter Courses: ")
    gpa = float(input("Enter GPA: "))
    sql = """
        UPDATE Student
        SET Name = %s, Department = %s, Courses = %s, GPA = %s
        WHERE StudentID = %s
    """
    cursor.execute(sql, (name, major, courses, gpa, sid))
    db.commit()
    print("Record updated!" if cursor.rowcount else "Student not found!")
def delete_stu():
    sid = int(input("Enter Student ID: "))
    sql = "DELETE FROM Student WHERE StudentID = %s"
    cursor.execute(sql, (sid,))
    db.commit()
    print("Record deleted!" if cursor.rowcount else "Student not found!")
def insert_faculty():
    fid = int(input("Enter Faculty ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    courses = input("Enter Courses Taught: ")
    sql = "INSERT INTO Faculty VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (fid, name, dept, courses))
    db.commit()
    print("Record inserted successfully!")
def display_faculty():
    cursor.execute("SELECT * FROM Faculty")
    for row in cursor.fetchall():
        print(row)
def update_fac():
    fid = int(input("Enter Faculty ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    courses = input("Enter Courses Taught: ")
    sql = """
        UPDATE Faculty
        SET Name = %s, Department = %s, CoursesTaught = %s
        WHERE FacultyID = %s
    """
    cursor.execute(sql, (name, dept, courses, fid))
    db.commit()
    print("Record updated!" if cursor.rowcount else "Faculty not found!")
def delete_fac():
    fid = int(input("Enter Faculty ID: "))
    sql = "DELETE FROM Faculty WHERE FacultyID = %s"
    cursor.execute(sql, (fid,))
    db.commit()
    print("Record deleted!" if cursor.rowcount else "Faculty not found!")

def create_objects():
    s1 = Student_Master(1, "Alice Johnson", "Computer Science", "DBMS, Algorithms", 3.8)
    s2 = Student_Master(2, "Bob Smith", "Electrical Eng", "Circuits, Signals", 3.2)
    s3 = Student_Master(3, "Carla Gomez", "Mathematics", "Calculus, Statistics", 3.9)
    s4 = Student_Master(4, "David Lee", "Physics", "Mechanics, Optics", 3.5)
    s5 = Student_Master(5, "Emma Brown", "Computer Science", "OS, Networks", 3.6)
    student_objects.append(s1)
    student_objects.append(s2)
    student_objects.append(s3)
    student_objects.append(s4)
    student_objects.append(s5)

    f1 = Faculty_Master(101, "Dr. Rao", "Computer Science", "DBMS, OS")
    f2 = Faculty_Master(102, "Dr. Patel", "Electrical Eng", "Circuits")
    f3 = Faculty_Master(103, "Dr. Chen", "Mathematics", "Calculus, Statistics")
    f4 = Faculty_Master(104, "Dr. Wilson", "Physics", "Mechanics, Optics")
    f5 = Faculty_Master(105, "Dr. Khan", "Computer Science", "Algorithms, Networks")
    faculty_objects.append(f1)
    faculty_objects.append(f2)
    faculty_objects.append(f3)
    faculty_objects.append(f4)
    faculty_objects.append(f5)
    print("Created 5 student objects and 5 faculty objects.")
def write_objects():
    if len(student_objects) == 0:
        print("No objects yet. Choose option 9 first.")
        return
    try:
        for s in student_objects:
            sql = "INSERT INTO Student VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (s.id, s.name, s.major, s.courses, s.cgpa))
        for f in faculty_objects:
            sql = "INSERT INTO Faculty VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (f.id, f.name, f.department, f.courses_taught))
        db.commit()
        print("Objects written to the database!")
    except mysql.connector.Error:
        db.rollback()
        print("Could not write. These IDs are probably already in the tables.")
def read_back():
    print("\n===== STUDENTS =====")
    cursor.execute("SELECT * FROM Student")
    for row in cursor.fetchall():
        s = Student_Master(row[0], row[1], row[2], row[3], row[4])
        print("Student ID:", s.id)
        print("Name:", s.name)
        print("Major:", s.major)
        print("Courses:", s.courses)
        print("CGPA:", s.cgpa)
        print()
    print("===== FACULTY =====")
    cursor.execute("SELECT * FROM Faculty")
    for row in cursor.fetchall():
        f = Faculty_Master(row[0], row[1], row[2], row[3])
        print("Faculty ID:", f.id)
        print("Name:", f.name)
        print("Department:", f.department)
        print("Courses taught:", f.courses_taught)
        print()

#Main Menu
while True:
    print("\n1. Insert Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Insert Faculty")
    print("6. Display Faculty")
    print("7. Update Faculty")
    print("8. Delete Faculty")
    print("9. Create 5 student & 5 faculty objects")
    print("10. Write objects to database")
    print("11. Read back from database and display all")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        insert_student()
    elif choice == "2":
        display_student()
    elif choice == "3":
        update_stu()
    elif choice == "4":
        delete_stu()
    elif choice == "5":
        insert_faculty()
    elif choice == "6":
        display_faculty()
    elif choice == "7":
        update_fac()
    elif choice == "8":
        delete_fac()
    elif choice == "9":
        create_objects()
    elif choice == "10":
        write_objects()
    elif choice == "11":
        read_back()
    elif choice == "0":
        break
    else:
        print("Invalid choice!")
cursor.close()
db.close()
print("Database connection closed.")

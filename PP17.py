

myStudents = {}
n = 1

def add_student():
    global n
    stu_name =  input("Please enter your name: ")
    lab1 = int(input("Please enter grade for Lab 1: "))
    lab2 = int(input("Please enter grade for Lab 2: "))
    lab3 = int(input("Please enter grade for Lab 3: "))
    lab4 = int(input("Please enter grade for Lab 4: "))
    lab5 = int(input("Please enter grade for Lab 5: "))
    total = lab1 + lab2 + lab3 + lab4 + lab5
    percent = (total / 500) * 100
    average = total / 5
    myStudents["Student" + str(n)] = {
        "name": stu_name,
        "Lab1": lab1,
        "Lab2": lab2,
        "Lab3": lab3,
        "Lab4": lab4,
        "Lab5": lab5,
        "Total": total,
        "Percent": percent,
        "Average": average
    }
    print("Added Student" + str(n))
    n = n + 1
def delete_student():
    num = int(input("Please enter the number of the student you wish to remove: "))
    myStudents.pop(num)
    print(myStudents)
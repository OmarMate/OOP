course1 = int(input("Enter the grade of the first class: "))
course2 = int(input("Enter the grade of the second class: "))
course3 = int(input("Enter the grade of the third class: "))

total = course1 + course2 + course3
percentile = (total/300) * 100

if percentile < 100 and percentile >= 90:
    print("Grade A")
elif percentile <= 90 and percentile >= 80:
    print("Grade B")
elif percentile <= 80 and percentile >= 70:
    print("Grade C")
elif percentile <= 70 and percentile >= 60:
    print("Grade D")
elif percentile <= 60 and percentile >= 50:
    print("Grade F")
else:
    print("Invalid grades")















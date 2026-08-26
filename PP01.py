print("Enter Employee's Name:")
emp_name = input()

print("Enter basic pay:")
basic_pay = int(input())

print("Enter deductions:")
deductions = int(input())

total_pay = basic_pay - deductions

print("The name of the employee is:", emp_name, " and the total pay is: ", total_pay)
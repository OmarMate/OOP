emp_pay = {}
n = 1
def add_emp():
    global n
    name = input("Enter employee name: ")
    base = int(input("Enter basic pay: "))
    allowance = int(input("Enter allowance: "))
    deductions = int(input("Enter deductions: "))
    taxes = int(input("Enter taxes: "))
    gross_pay = base + allowance
    net_pay = gross_pay - deductions - taxes
    emp_pay["Employee" + str(n)] = {
        "Name" : name,
        "Base" : base,
        "Allowance" : allowance,
        "Deductions" : deductions,
        "Taxes" : taxes,
        "Gross Pay" : gross_pay,
        "Net Pay" : net_pay
    }
    n = n + 1
    print("Alright they're added!")
def del_emp():
    num = int(input("Please enter the number of the employee you wish to remove: "))
    emp = "Employee" + str(num)
    emp_pay.pop(emp)
    print("Employee has been removed!")
def mod_emp():
    num = int(input("Please enter the number of the employee you wish to modify: "))
    emp = "Employee" + str(num)
    emp_pay[emp]["Base"] = int(input("Please enter new base pay: "))
    emp_pay[emp]["Allowance"] = int(input("Please enter new allowance: "))
    emp_pay[emp]["Deductions"] = int(input("Please enter new deductions: "))
    emp_pay[emp]["Taxes"] = int(input("Please enter new taxes: "))
    gross_pay = emp_pay[emp]["Base"] + emp_pay[emp]["Allowance"]
    net_pay = emp_pay[emp]["Deductions"] - emp_pay[emp]["Taxes"]
    emp_pay[emp]["Gross Pay"] = gross_pay
    emp_pay[emp]["Net Pay"] = net_pay
    print("Employee info has been updated!")
def display_emp():
    print("Here are all the employees:")
    print(emp_pay)
def exit_emp():
    print("Thank you for using our application!")
    exit()
while True:
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Modify Employee")
    print("4. Display Employees")
    print("5. Exit")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        add_emp()
    elif choice == 2:
        del_emp()
    elif choice == 3:
        mod_emp()
    elif choice == 4:
        display_emp()
    elif choice == 5:
        exit_emp()
    else:
        print("Please enter a valid choice!")
        continue





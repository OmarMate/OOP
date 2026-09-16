while (True):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Exit")
    choice = input("Enter your choice: ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if choice == "1":
        c = num1 + num2
        print(c)
    elif choice == "2":
        c = num1 - num2
        print(c)
    elif choice == "3":
        c = num1 * num2
        print(c)
    elif choice == "4":
        c = num1 / num2
        print(c)
    elif choice == "5":
        a = "Yes" & "No"
        print("DO WANT TO EXIT? Yes or No")
        if a == "Yes":
            exit()

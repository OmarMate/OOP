empList = []
while True:
    print("1. Add an Element to the list")
    print("2. Remove an Element from the list")
    print("3. Replace an Element in the list")
    print("4. Sort the Elements in the list")
    print("5. Print the Elements in the list")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        empList.append(int(input("Enter a number: ")))
        print(empList)
    elif choice == 2:
        empList.remove(num)
        print(empList)
    elif choice == 3:
        new_num = int(input("Enter a new number: "))
        index = empList.index(num)
        empList[index] = new_num
        print(empList)
    elif choice == 4:
        empList.sort()
        print(empList)
    elif choice == 5:
        for i in range(len(empList)):
            print(empList[i])
    elif choice == 6:
        break
    else:
        print("Invalid Input")
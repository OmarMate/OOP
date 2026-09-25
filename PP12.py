mycourses = {}
i = 1
while True:
    print("1. Add Course")
    print("2. Remove Course")
    print("3. Replace Course")
    print("4. Print Course")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        course_name = input("Enter your course name: ")
        mycourses.update({"c_name"+str(i):course_name})
        i = i+1
        print(mycourses)
    elif choice == "2":
        num = ('c_name'+input("Enter the number of the course you wish to remove: "))
        del mycourses[num]
        print(mycourses)
    elif choice == "3":
        num = ('c_name'+input("Enter the number of the course you wish to replace: "))
        mycourses[num] = input("Enter the new course name: ")
        print(mycourses)
    elif choice == "4":
        print("Here are your current courses: ", mycourses)
    elif choice == "5":
        print("Goodbye")
        exit()
    else:
        print("Please enter a valid input. If not, the program won't work.")
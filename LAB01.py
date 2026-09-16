while (True):
    print("1. Area of rectangle")
    print("2. Volume of a Cube")
    print("3. Area of a Circle")
    print("4. Circumference of a Circle")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        l = int(input("Enter the length: "))
        w = int(input("Enter the width: "))
        Area = l * w
        print("The Area of the rectangle: ", Area)
    elif choice == "2":
        l = int(input("Enter the length: "))
        w = int(input("Enter the width: "))
        h = int(input("Enter the height: "))
        Volume = l * w * h
        print("The Volume of the rectangle: ", Volume)
    elif choice == "3":
        r = int(input("Enter the radius: "))
        AreaOfCircle = 3.13 * r**2
        print("The Area of the circle: ", AreaOfCircle)
    elif choice == "4":
        r = int(input("Enter the radius: "))
        Cfm = 2 * 3.14 * r
        print("The Circumference of the circle: ", Cfm)
    elif choice == "5":
        exit()
    else:
        print("Invalid Input")
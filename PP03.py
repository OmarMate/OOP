num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

if num1 > num2 and num1 > num3:
    print("Number1 is the biggest")
elif num2 > num1 and num2 > num3:
    print("Number2 is the biggest")
elif num3 > num1 and num3 > num2:
    print("Number3 is the biggest")

if num1 < num3 and num1 < num2:
    print("Number1 is smallest")
elif num2 < num1 and num2 < num3:
    print("Number2 is smallest")
elif num3 < num1 and num3 < num2:
    print("Number3 is smallest")
elif num1 == num2 and num1 == num3:
    print("All numbers are the same")
else:
    print("Invaild numbers")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter the operator: ")

if operator == "+":
    a = num1 + num2
    print("The result is: ", a)
elif operator == "-":
    b = num1 - num2
    print("The result is: ", b)
elif operator == "*":
    c = num1 * num2
    print("The result is: ", c)
elif operator == "/":
    d = num1 / num2
    print("The result is: ", d)
elif operator == "%":
    e = num1 % num2
    print("The result is: ", e)
if num1 or num2 == 0:
    print("Cannot divide by zero")






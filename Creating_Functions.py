def add():
    a = int(input())
    b = int(input())
    c = a + b
    print(c)

def sub():
    a = int(input())
    b = int(input())
    c = a - b
    print(c)

def mul():
    a = int(input())
    b = int(input())
    c = a * b
    print(c)

def div():
    a = int(input())
    b = int(input())
    c = a / b
    print(c)

# Main Code

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    add()
elif choice == 2:
    sub()
elif choice == 3:
    mul()
elif choice == 4:
    div()
elif choice == 5:
    print("Goodbye!")
    exit()
else:
    print("Invalid choice")
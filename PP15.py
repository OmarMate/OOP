myQueue = []

def enqueue():
    obj = input("Enter the name of new object: ")
    myQueue.append(obj)
    print(myQueue)
def dequeue():
    myQueue.pop(0)
    print(myQueue)
def display_queue():
    print(myQueue)

while True:
    print("1. Add to queue")
    print("2. Remove from queue")
    print("3. Display queue")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display_queue()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Please enter a valid choice!")

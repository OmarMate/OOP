a = [2, 56, 43, 18, 29, 16]
a.append(66) #lets you add an element to list
print(a)
a.remove(56) #lets you remove an element from list
print(a)
a.pop()  #lets you remove the last element from list
print(a)
a.sort() #lets you sort the list in by numerical order
print(a)
b = a.copy() #lets you copy the list and add it to the list
b.append(1001)

newVal = int(input("Enter a number: "))
if newVal in a:
    print("The element is in the list")
else:
    print("The element is not in the list")
















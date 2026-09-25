myDictionary = {"name1":"Justus", "name2":"Jim", "name3":"Joe"}
print(myDictionary)
myDictionary.update({"name4":"Joseph"}) #Lets you add a value into the dictionary
print(myDictionary)
del myDictionary["name2"] #Lets you delete a value from the dictionary
myDictionary["name4"] = "Melba" #Lets you replace a value from dictionary
print(myDictionary)

fullname = input("Enter your full name: ")
myDictionary.update({"name5":fullname}) #Uses users input to update value

mycourses = {"c_name1":"OOP"}


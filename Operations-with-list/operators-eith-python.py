myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

newList= myList[0:9]

for i in myList:
    if 1 in newList:
        del myList[1]

print("The list with unique elements only:")
print(myList)
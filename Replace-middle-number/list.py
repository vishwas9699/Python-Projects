hatList = [1,2,3,4,5]

UserNumber = int(input("Give me a number for the middle:"))
hatList[2]=UserNumber
del hatList[4]
print(len(hatList))
print(hatList)
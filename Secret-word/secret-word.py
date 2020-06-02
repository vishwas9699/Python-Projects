animal = input("Please choose animal:")
while animal != "chupacabra":
    if animal == "chupacabra":
        break
    else:
        print("wrong animal, pick again")
        animal = input("Please choose animal:")
else:
    print("nice")        
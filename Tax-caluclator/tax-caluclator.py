income = float(input("Enter the annual income: "))
if income<=85528:
    tax=income*.18-556.02
else:
    surplus=(income-85528)*.32
    tax=14839.02+surplus

if tax<1:
     tax=0.0       

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
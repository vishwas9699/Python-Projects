year = int(input("Enter a year: "))

if year<1582:
    print("Not within the gregorisn calender period")
elif int(year%4)!=0:
    print("Commom Year")
elif int(year%100)!=0:
    print("Leap Year")
elif int(year%400)!=0:
    print("Common Year")
else:
    print("Leap year")        
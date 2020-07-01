# Numbers Processor

line = input("Enter a line of numbers - separate them with spaces: ") # ask the user to enter a line filled with any number of numbers (the numbers can be floats)
strings = line.split() # split the line receiving a list of substrings;
total = 0 # initiate the total sum to zero;
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")
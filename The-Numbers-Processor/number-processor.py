# Numbers Processor

line = input("Enter a line of numbers - separate them with spaces: ") # ask the user to enter a line filled with any number of numbers (the numbers can be floats)
strings = line.split() # split the line receiving a list of substrings;
total = 0 # initiate the total sum to zero;
try: # as the string-float conversion may raise an exception, it's best to continue with the protection of the try-except block;
    for substr in strings: # iterate through the list...
        total += float(substr) #  ...and try to convert all its elements into float numbers; if it works, increase the sum;
    print("The total is:", total) # everything is good so far, so print the sum;
except:
    print(substr, "is not a number.")
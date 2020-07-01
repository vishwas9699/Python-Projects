text = input("Enter your message: ") # ask the user to enter the open (unencrypted), one-line message;
cipher = '' #prepare a string for an encrypted message (empty for now)
for char in text:  #start the iteration through the message;
    if not char.isalpha():  # if the current character is not alphabetic...
        continue   # ...ignore it;
    char = char.upper()   #  convert the letter to upper-case (it's preferable to do it blindly, rather than check whether it's needed or not)
    code = ord(char) + 1   # get the code of the letter and increment it by one;
    if code > ord('Z'):  # if the resulting code has "left" the Latin alphabet (if it's greater than the Z code)...
        code = ord('A')  # ...change it to the A code;
    cipher += chr(code)  # append the received character to the end of the encrypted message;
print(cipher)  # print the cipher.
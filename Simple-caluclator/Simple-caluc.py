import os
clear = lambda: os.system('cls') 
clear()
print("Hello and welcome to this simple calculator\n ")
ch=1
while(ch==1):

        print("Please choose the operations which you want to perform")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Quit Calculator")    
        c=0
        def add( a, b): #Function for Addition
            c=a+b
            return c
        
        def sub( a, b): #Function for Subtraction
            c=a-b
            return c
        
        def multi( a, b):#Function for Multiplication
            c=a*b
            return c
        
        def divi( a, b):#Function for Division
            c=a/b
            return c    
            
        x=float(input("Enter the Value of A:- "))
        y=float(input("Enter the Value of B:- "))
        choice=int(input("Enter the choice which you want to perform:- "))
        result=0
        try:
           if choice==1:
            result=sum(x,y)
            print("The result is:-",result) 
           elif choice==2:
                result=sub(x,y)
                print("The result is:-",result)             
           elif choice==3:
                result=multi(x,y)
                print("The result is:-",result) 
           elif choice==4:
                if(y==0):
                   print("Cannot divide it by zero")
                else:
                    result=divi(x,y)
                    print("The result is:-",result) 
           elif (choice==5):
                ch=0
           else:
                  print("%d is not valid input. Please enter 1, 2 ,3 ,4 or 5." % choice)
        except ValueError:
          print("%r is not valid input.  Please enter 1, 2, 3, 4 or 5.",choice)
          print("Thank you for using this calculator!")   
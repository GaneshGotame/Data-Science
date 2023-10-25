#if else conditional statement

a=input("Enter any number :")
a=int(a)
if(a>0):
    print("The number is positive")
    if(a%2==0):
        print("The number is even")
    else:
        print("The number is odd")
elif(a==0):
    print("The number is zero")
    
else:
    print("The number is negative")
    
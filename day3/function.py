#functions
def greater(a,b):
    if(a==b):
        print("Both are equal")
    elif(a>b):
        print(a," is greater than ",b)
    else:
        print(b," is greater than ",a)
    
x=int(input("Enter the value of x :"))
y=int(input("Enter the value of y :"))
greater(x,y)

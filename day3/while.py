#while loop
'''i=0;
while(i<18):
    i=int(input("Enter your age:"))
    print("You can't enter")
print("You can enter")
'''
i=0
while(i<=12):
    i=i+1
    if(i==11):
        break
    
    if(i==5):
        print("skip the iteration")
        continue
    print("8 * ",i,"=",i*8)
    
print("Code run upto i = 10")
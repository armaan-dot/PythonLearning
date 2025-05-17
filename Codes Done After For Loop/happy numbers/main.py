

print("CODE TO CHECK IF A NUMBER IS HAPPY OR UNHAPPY")
i=int(input("ENTER YOUR NUMBER"))
a=i
a1=a//10
a2=a%10
a3=a2*a2
a4=a1*a1
while i!=1 and i!=4:
    if a3+a4 == 1:
        print(i,"is a happy number")
        break
    else:
        print(i,"is not a happy number")
        break
        
    
    

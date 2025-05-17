

print("To Find HCF Of Two Numbers ")
a=int(input("Enter Your First Number"))
b=int(input("Enter Your Second Number"))
if a>b:
    for n in range(2,b):
        if a%n==0 and b%n==0:
            print(n,"are the common factors")
        
             
            
if b>a:
    for n in range(2,a):
        if b%n==0 and a%n==0:
            print (n,"is gcd")
            

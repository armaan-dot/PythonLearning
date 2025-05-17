
print("code to find automorphic numbers")
a=int(input("enter your number"))
a1=a*a
n=10
b=0
b1=0
auto=a1
while a1>=0:
    b=auto%n
    if b==a1:
        b1=1
        break
    a1=a1%n
    n=n*10
if b1==1:
    print("no. is automorphic")
else:
    print("no. is not automorphic")
    


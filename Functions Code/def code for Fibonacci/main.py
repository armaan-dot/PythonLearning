
a=int(input("your number"))
def f(n1,n2,n):
    n1=0
    n2=1
    s = 0
    for n in range(a):
        print(n1)
        s=n1  
        n1=n2  
        n2=s+n1 
f(0,0,0)




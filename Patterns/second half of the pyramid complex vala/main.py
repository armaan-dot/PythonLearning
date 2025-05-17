
x=65
sum=chr(x)
x1=65
sum1=chr(x1)
x2=65
sum2=chr(x2)
for r in range(0,4):       
    for c in range(4-r):
        print(" ",end="" )
    for c in range(0,r+1):
        print(sum1,end="")
        x1=x1+1
        sum1=chr(x1)
    x2=x1-2
    for c in range(0,r):
        sum2=chr(x2)
        print(sum2,end="")
        x2=x2-1
        
    print()
    x1=65
    sum1=chr(x1)
    
    sum2=chr(x2)




x=65
sum=chr(x)
x1=66
sum1=chr(x1)
x2=x1-1
sum2=chr(x2)
for r in range(0,4):       
    for c in range(4-r):
        print(" ",end="" )
    for c in range(0,1):
        print(sum,end="")
    for c in range(0,r):
        print(sum1,end="")
        x1=x1+1
        sum1=chr(x1)
    for c in range(0,r):
        print(sum2,end="")
        x2=x1-1
        sum2=chr(x2)
    print()
    x1=66
    sum1=chr(x1)
    x2=65
    sum2=chr(x2)


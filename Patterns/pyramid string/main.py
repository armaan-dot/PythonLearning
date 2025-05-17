
x=65
sum=chr(x)
for r in range(0,5):
    for c in range(0,5-r):
        print(" ",end="")
    for c in range(0,r+1):
        print(sum,end=" ")
        x=x+1
        sum=chr(x)
    print()

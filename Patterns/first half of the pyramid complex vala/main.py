'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

x=65
sum=chr(x)
x1=66
sum1=chr(x1)
for r in range(0,4):       
    for c in range(4-r):
        print(" ",end="" )
    for c in range(0,1):
        print(sum,end="")
    for c in range(0,r):
        print(sum1,end="")
        x1=x1+1
        sum1=chr(x1)
    print()
    x1=66
    sum1=chr(x1)

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
x=65
sum=chr(x)
for r in range(0,5):
    for c in range(0,6-r-1):
        if x>=66:
            print(" ",end="")
        else:
            print(" ",end="")
    for c in range(0,r+1):
        if x>=66:
            print(sum,end=" ")
        else:
            print(sum,end="  ")
        
        x=x+1
        sum=chr(x)
    print()






'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
print("To Find HCF Of Two Numbers ")
a=int(input("Enter Your First Number"))
b=int(input("Enter Your Second Number"))
d=0
while a%b !=0:
    d=a%b
    a=b
    b=d
    
print("G.C.D =",b)
        
    


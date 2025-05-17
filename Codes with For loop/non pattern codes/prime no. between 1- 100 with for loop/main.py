'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
  
  
   
for n in range(1,100):
    b=0  
    for c in range(1,n+1):
        if n%c==0 :
            b=b+1 
    if b==2:
        print (n)
    


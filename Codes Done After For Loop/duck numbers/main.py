

a=0
b=0
print("CODE TO FIND IF A NUMBER IS DUCK NUMBER OR NOT ")
a1=int(input("PLEASE ENTER A NUMBER "))
i=a1
while i>0: 
    a=i%10 
    if a==0:     
        b=1     
        break  
    i=i//10
if b==1:   
    print(a1," IS A DUCK NUMBER")
else:
    print(a1," IS NOT A DUCK NUMBER")



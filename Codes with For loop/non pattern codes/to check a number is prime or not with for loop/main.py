#this code is made by kidstokid_
#please subscribe to our channel kidstokid_

print("To check no. is prime or not")
a=int(input("Enter the no."))
if a>=1:
    for n in range(2,a):
        if a%n == 0:
            print(a,"is not a prime no.")
            break
    else :
        print(a,"is a prime no.")
    




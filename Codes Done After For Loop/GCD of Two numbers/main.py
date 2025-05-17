
c=0
print("To Find HCF Of Two Numbers ")
a = int(input("Enter your first number: "))
b = int(input("Enter your second number number: "))
i = 1
while(i <= a and i <= b):
  if(a % i == 0 and b % i == 0):
    c = i
  i = i + 1
print("GCD is", c)

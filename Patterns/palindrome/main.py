

x=input("enter your word-")
v=len(x)
for i in range(v-1,-1,-1):
    a=(x[i])
    if a==x[v-1-i]:
        t=0
    else:
        t=1
if t==0:
    print("yes,your number is a palindrome")
elif t==1:
    print("no,your number is not a palindrome")
print("  ")
x1=input("DO YOU WANT TO PRINT YOUR REVERSED WORD,")
if x1=="yes":
    for i in range(v-1,-1,-1):
       print(x[i],end="")

    




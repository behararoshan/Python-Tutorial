n=int(input())
if(n%2==0):
    print("weird number")
elif (n%2==0) and (2<=n<=5):
    print(" not weird")
elif (n%2==0) and (6<=n<=20):
    print("weird number")
else:
    print("not")
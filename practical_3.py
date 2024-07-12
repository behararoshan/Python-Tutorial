n=int(input("enter the num "))
if n>1:
    for i in range (2,n):
        if(n%i)==0:
            print("no. is not a prime: ")
            break
    else:
        print("no. is a prime: ")
else:
    print("not prime")            

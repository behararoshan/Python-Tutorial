import mailcap


def gcd(a,b):
    min=a
    if(b<a):
        min=b

    for i in range(1,min+1):
        if(a%i==0 and b%i==0):
            hcf=i
    return(hcf)
print(gcd(10,25))
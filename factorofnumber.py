def factors(h):
    for i in range(1,h+1):
        if(h%i==0):
            print(i)
print(factors(15))
print(factors(20))
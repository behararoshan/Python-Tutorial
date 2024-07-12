'''n=int(input())
if(n==1):
    print(0)
else:
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c'''
    
'''n=int(input())
a=0
b=1
print(a)
print(b)
count=1
while(count<=n-2):
    c=a+b
    print(c)
    count=count+1
    a=b
    b=c'''

'''n=int(input())
if(n==1):
    print(0)
else:
    a=0
    b=1
    print(a)
    print(b)
    while(n>2):
        c=a+b
        print(c)
        a=b
        b=c'''





n=int(input())
flag=0
while flag<2:
    flag+=1
    count=1
    while count<=n:
        print("* "*count)
        count=count+1

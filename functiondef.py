'''def myfunction (country="swedan"):
       print("i am from country ",country)
myfunction("indian")       
myfunction(    )
myfunction(  "nfhkfkjshfkjkjhdnkjhkkjnfkj")'''


#arbitary arugment in python
'''def myfunction (*t):
    print("yougest is",t[2])
myfunction("saikiran","yamini","yajna")'''


#write a function sum all that take any member of arugment and return there sum #

from binascii import b2a_hqx


''''def sumall(*t):
    sum=0
    i=0
    while(i<len(t)):
        sum=sum+t[i]
        i=i+1
    print(sum)
sumall(1,2,3,4,5,6)'''

#consider the tuple (1,3,5,7,9,2,4,6,8,10) write a program to print the half line another half line in second line? #

#consider ' ' (12,7,38,56,78) write a program to print another tuple whose valuse are even number in given number? 
b=[]
a=[1,2,3,4,5,6,7,]
for i in a:
    if (i%2==0):
        b.append(i)
a=tuple(b)
print(a)
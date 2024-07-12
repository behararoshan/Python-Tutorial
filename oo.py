
'''s=input()
d={"letters":0,"digits":0}
for c in s:
    if c.isalpha():
        d["letters"]+=1

    elif c.isdigit():
        d["digits"]+=1
    
    else:
        pass
    print("letters",d["letters"])
    print("digits",d["digits"])'''



'''s=input()
d={"upper_case":0,"lower_case":0}
for c in s:
    if c.isupper():
        d["upper_case"]+=1

    elif c.islower():
        d["lower_case"]+=1
    
    else:
        pass
    print("upper_case",d["upper_case"])
    print("lower_case",d["lower_case"])'''


    f=("ABC.txt","w")
    f.write("india is great")
    f.close()
    f=open("ABC.txt","r")
    print(f.read(10))
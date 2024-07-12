def fact_function(n):
    f=1
    for i in range(1,n+1):
        f=i*f
    return(f)

print("factorial= ",fact_function(5))

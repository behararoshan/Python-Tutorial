#program to short a list of nsmes in ascending order?

'''n=int(input("enter the no names: "))
name=[]
for i in range(n):
    name.append(input("enter the name: "))
print(name)
print(sorted(name))'''

#WAP to read a set of numbers from keyboard & to find the sum of all elements of the given array using a function.?

def _sum(arr):
  sum =0
  for i in arr:
    sum=sum+i
  return(sum)
  
arr = []
n=int(input("enter numbers: "))
for i in range(n):
    new_var = arr.append(int(input("enter number: ")))
print(arr)
ans=_sum(arr)
print("sum of the array is:",ans)







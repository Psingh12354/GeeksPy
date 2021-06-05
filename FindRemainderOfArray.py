from functools import reduce
arr=[100,10,5,25,35,14]
n=int(input("Enter the number : "))
print((reduce(lambda x,y : x*y,arr))%n) 

#Filter
def is_even(n):
    if n%2==0:
        return True
nums=[1,2,3,4,5,6,7,8,9]
evens = list(filter(is_even,nums))
print(evens)

#or
evens = list(filter(lambda n: n%2==0,nums))
print(evens)

#Map change every value
print(list(map(lambda x : x+2,evens)))

#Reduce
print(reduce(lambda a,b : a+b,evens)) 

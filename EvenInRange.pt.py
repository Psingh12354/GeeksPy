list1 = [10, 21, 4, 45, 66, 93, 11]
n1=int(input("Enter number 1 : "))
n2=int(input("Enter number 2 : "))
evens=list(lambda n1,n2 : (for num in range(n1,n2+1): if num%2==0))
print(evens)

list1 = [10, 21, 4, 45, 66, 93, 11,12]
n1=int(input("Enter number 1 : "))
n2=int(input("Enter number 2 : "))
evens=list(filter(lambda x :  x%2==0,list1[n1:n2+1]))
print(evens)

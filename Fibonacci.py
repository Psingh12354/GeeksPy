n=int(input("Enter number : "))
a=0
b=1
if n<0:
    print("Wrong input")
elif n==1:
    print('0')
elif n==2:
    print('1')
else:
    for i in range(2,n):
        c=a+b
        a,b=b,c
    print(b)

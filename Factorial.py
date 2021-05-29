# 1>
def fact(n):
    return 1 if (n==1 or n==0) else n*fact(n-1)
n=5
print(fact(n))

# 2>
n=5
product=1
for i in range(1,n+1):
    product*=i
print(product)

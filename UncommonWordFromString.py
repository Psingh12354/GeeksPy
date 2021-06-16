a="apple banana mango" 
b="banana fruits mango"
a=a.split()
b=b.split()
k=set(a).symmetric_difference(set(b))
print(k)

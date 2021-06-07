list1 = [10, 21, 4, 45, 66, 93, 11,12]
list2=[]
list2.extend(list1)
print(list2)
# Or
del list2[:]
list2=[]
list2=list1[:]
print(list2)

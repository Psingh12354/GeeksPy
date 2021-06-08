list1 = [10, 20, 30, 40, 50]
list2 = []
count=0
for i in range(len(list1)):
    if i==0:
        count=list1[i]
        list2.append(count)
    if i>0:
        count+=list1[i]
        list2.append(count)
print(list2)
        

list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
list2 = []
for i in list1:
    if list1.count(i)>1:
        list2.append(i)
print(set(list2))

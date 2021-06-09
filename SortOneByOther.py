list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2, 0, 1]
zipped=zip(list2,list1)
z=[i for _,i in sorted(zipped)]
print(z)

# A list whose all element follow the same order either asscend or descend is monotonic
arr=[5,15,20,10]
var=True
for i in range(len(arr)-1):
    if arr[i]<=arr[i+1]:
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                var=False
    else:
        for j in range(i,len(arr)):
            if arr[i]<arr[j]:
                var=False
print(var)

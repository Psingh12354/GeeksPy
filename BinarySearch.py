pos=-1
def search(list1,n):
    l=0
    u=len(list1)-1
    while l<=u:
        mid=(l+u)//2
        if list1[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list1[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list1=[5,4,3,7,8,0]
n=8
if search(list1,n):
    print("found ",pos)
else:
    print("not found")
        

pos=-1
def search(list1,n):
    i=0
    while i<len(list1):
        if list1[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False
list1=[5,4,3,7,8,0]
n=8
if search(list1,n):
    print("found ",pos)
else:
    print("not found")
        

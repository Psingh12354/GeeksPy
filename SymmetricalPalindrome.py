string='khokho'
if string==string[::-1]:
    print("Palindrome Yes")
else:
    print("Palindrome No")
n = len(string)
flag = 0
if n%2:
    mid_val = n//2 +1
else:
    mid_val = n//2
start1=0
start2=mid_val
while start1 < mid_val and start2 < n:
    if string[start1]==string[start2]:
        start1+=1
        start2+=1
    else:
        flag=1
        break
if flag==0:
    print("Symmetrical")
    
    

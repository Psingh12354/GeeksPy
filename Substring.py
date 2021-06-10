string = "geeks for geeks"
sub_str ="geek"
if string.find(sub_str)==-1:
    print("No")
else:
    print("Yes")

# or

if string.count(sub_str)>0:
    print("Yes")
else:
    print("No")

num=153
stringSize=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**stringSize
    temp//=10
if num==sum:
    print("Arm")
else:
    print("Not Arm")

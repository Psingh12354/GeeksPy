s = "GeeksforGeeks"
n=int(input("Enter the number : "))
string1=s[n+1:]+s[:n]
string2=s[n:]+s[:n]
print("Left ",string1)
print("Right ",string2)

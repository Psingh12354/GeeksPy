s=str("Hello World")
print(s)
inp=input("Enter character : ")
if inp in s:
    val=s.count(inp)
    print("Element found : ",val)

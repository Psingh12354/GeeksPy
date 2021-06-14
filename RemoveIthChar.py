inp="geeks"
n=int(input("Enter the number : "))
if n>len(inp):
    print("Wrong Input")
else:
    inp=inp.replace(inp[n],"",1)
print(inp)

#or
inp1="geeks"
n=int(input("Enter the number : "))
if n>len(inp):
    print("Wrong Input")
else:
    a=inp[:n]
    b=inp[n:]
print(a+b)

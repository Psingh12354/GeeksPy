string = "hello geeks for geeks is computer science portal"
k=int(input("Enter the size : "))
storage=[]
text=string.split(" ")
for i in text:
    if len(i)>k:
        storage.append(i)
print(storage)

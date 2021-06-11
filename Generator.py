#generator doesn't load all value at a time one by one
def topten():
    n=1
    while n<=10:
        sq=n**2
        yield sq
        n+=1
values=topten()
for i in values:
    print(i)

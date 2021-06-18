from collections import Counter
def duplicate(input1):
    list = []
    wc=Counter(input1)
    for key,val in wc.items():
        if val>1:
            list.append(key)
            print(list)
input1="Priyanshu"
duplicate(input1)

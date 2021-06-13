from collections import Counter
string="GeeksforGeeks"
res=dict(Counter(string))
print(min(res,key=res.get))

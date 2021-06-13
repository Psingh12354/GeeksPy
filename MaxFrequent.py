from collections import Counter
string="GeeksforGeeks"
res=dict(Counter(string))
print(max(res,key=res.get))

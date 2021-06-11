from collections import Counter
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
res=Counter(test_str.split())
print("The word frequency is : "+str(res))

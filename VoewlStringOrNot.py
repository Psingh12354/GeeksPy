from collections import Counter
string='ABeeIghiObhkUul'
string = string.replace(' ', '')
string = string.lower()
vowel = [string.count('a'), string.count('e'), string.count('i'), string.count('o'), string.count('u')]
if vowel.count(0)>0:
   print('not accepted')
else:
    print('accepted')

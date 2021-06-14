import re
string = "Geeks$For$Geeks"
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if regex.search(string)==None:
    print("String accepted")
else:
    print("Not accepted")

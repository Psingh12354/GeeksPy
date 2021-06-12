str1 = 'abcdef'
str2 = 'defghia'
set_str1=set(str1)
set_str2=set(str2)
matched=set_str1 & set_str2
print("No of matching character : "+str(len(matched)))

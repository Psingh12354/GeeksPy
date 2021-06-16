n='01'
string = "001021010001010"
for char in string:
    if char not in n:
        print("Not a Binary String")
        break
    else:
        print("Binary String")
        break

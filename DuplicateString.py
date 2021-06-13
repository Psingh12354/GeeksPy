from collections import OrderedDict
string="helloworld"
print("Without Ordered : ","".join(set(string)))
print("Ordered : ","".join(OrderedDict.fromkeys(string)))

a=5
b=0
try:
    print("Resouce Open")
    print(a/b)
except Exception as e:
    print("An Error occurred : ",e)
finally:
    print("resource close")

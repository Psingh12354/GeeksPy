for i in range(11,25):
    for j in range(2,i//2):
        if i%j==0:
            break
    else:
        print(i)

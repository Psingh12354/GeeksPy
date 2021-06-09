n=int(input("Enter number of rows : "))
m=int(input("Enter number of column : "))
matrix=[]
for i in range(n):
    a=[]
    for j in range(m):
        a.append(int(input()))
    matrix.append(a)
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=' ')
    print()

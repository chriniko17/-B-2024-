def find(n):
    a=[[0]*(n+1) for i in range(n+1)]
    for i in range(n+1):
        a[0][i]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,min(i,j)+1):
                a[i][j]+=a[i-k][k]
    #print(a)
    return a[n][n]
while True:
    try:
        n = int(input())
        print(find(n))
    except EOFError:
        exit()
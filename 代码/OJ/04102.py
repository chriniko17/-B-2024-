k,m,n=map(int,input().split())
a=[[float("-inf")]*(n+1) for i in range(m+1)]
a[m][0]=k
for _ in range(n):
    q,p=map(int,input().split())
    for i in range(1,m-p+1):
        for j in range(n,-1,-1):
            if a[i+p][j-1]>=q:
                a[i][j]=max(a[i][j],a[i+p][j-1]-q)
for i in range(n,-1,-1):
    for j in range(m,-1,-1):
        if  a[j][i]!=float("-inf"):
            print(i,j)
            exit()


def count1(a,i,j):
    return [a[i-1][j],a[i+1][j],a[i][j-1],a[i][j+1],a[i-1][j-1],a[i-1][j+1],a[i+1][j-1],a[i+1][j+1]].count(1)
n,m=map(int,input().split())
a=[[-1]*(m+2) for i in range(n+2)]
ans=[[-1]*(m+2) for i in range(n+2)]
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(m):
        a[i+1][j+1]=l[j]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]==0:
            if count1(a,i,j)==3:
                ans[i][j]=1
            else:
                ans[i][j]=0
        else:
            if count1(a,i,j)==2 or count1(a,i,j)==3:
                ans[i][j]=1
            else:
                ans[i][j]=0
for i in range(1,n+1):
    print(" ".join(map(str,ans[i][1:m+1])))
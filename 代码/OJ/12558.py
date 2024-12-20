n,m=map(int,input().split())
a=[[0]*(m+2) for i in range(n+2)]
for i in range(1,n+1):
    temp=list(map(int,input().split()))
    for j in range(1,m+1):
        a[i][j]=temp[j-1]
ans=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]==1:
            if a[i-1][j]==0:
                ans+=1
            if a[i+1][j]==0:
                ans+=1
            if a[i][j-1]==0:
                ans+=1
            if a[i][j+1]==0:
                ans+=1
print(ans)
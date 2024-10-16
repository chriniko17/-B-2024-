def clear(a,x,y,d):
    ans=0
    for i in range(x-d,x+d+1):
        for j in range(y-d,y+d+1):
            ans+=a[i][j]
    return ans
a=[[0]*1025 for i in range(1025)]
d=int(input())
n=int(input())
for _ in range(n):
    x,y,i=map(int,input().split())
    a[x][y]=i
ans=0
for i in range(d,1025-d):
    for j in range(d,1025-d):
        ans=max(ans,clear(a,i,j,d))
print(ans)
n=int(input())
a=list(map(int,input().split()))
up=[1]*n
down=[1]*n
for i in range(n):
    for j in range(i):
        if a[j]<a[i]:
            up[i]=max(up[i],up[j]+1)
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if a[j]<a[i]:
            down[i]=max(down[i],down[j]+1)
ans=max(up[i]+down[i]-1 for i in range(n))
print(ans)
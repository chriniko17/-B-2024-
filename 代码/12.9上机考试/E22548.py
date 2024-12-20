a=list(map(int,input().split()))
n=len(a)
max_rec=[float("-inf")]*(len(a))
max_rec[n-1]=a[n-1]
for i in range(n-2,-1,-1):
    max_rec[i]=max(max_rec[i+1],a[i])
ans=0
for i in range(n):
    ans=max(ans,max_rec[i]-a[i])
print(ans)
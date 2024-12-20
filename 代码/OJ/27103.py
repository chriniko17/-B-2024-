n,m=map(int,input().split())
a=list(map(int,input().split()))
d=set()
ans=0
for i in range(n):
    if a[i] not in d:
        d.add(a[i])
    if len(d)==m:
        ans+=1
        d.clear()
print(ans+1)

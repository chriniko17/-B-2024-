n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
k=n
for i in range(n):
    if a[i]>=0:
        k=i
        break
print(-sum(a[0:min(m,k)]))

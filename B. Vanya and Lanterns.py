n,l=map(int,input().split())
a=sorted(list(map(int,input().split())))
d=0
for i in range(n-1):
    d=max(d,a[i+1]-a[i])
print(max(d/2,a[0],l-a[n-1]))
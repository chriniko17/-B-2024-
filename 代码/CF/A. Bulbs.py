n,m=map(int,input().split())
a=[0]*m
for _ in range(n):
    c=list(map(int,input().split()))[1::]
    for j in range(len(c)):
        a[c[j]-1]=1
if a.count(0)!=0:
    print("NO")
else:
    print("YES")
n,m=map(int,input().split())
a=[0]*m
a[0],a[1]=1,1
for i in range(1,n):
    k=sum(a)
    for j in range(m-1,0,-1):
        a[j]=a[j-1]
    a[0]=k
    #print(a)
print(sum(a))
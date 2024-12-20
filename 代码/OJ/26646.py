n,m=map(int,input().split())
a=[]
na=[]
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(max(a[i][0],a[i][1]-1),min(m,a[i][0]+a[i][1])):
        na.append([j-a[i][1]+1,j])
na.sort(key=lambda x:(x[1],x[0]))
mark=na[0][1]
ans=1
for i in range(1,len(na)):
    if na[i][0]>mark:
        ans+=1
        mark=na[i][1]
print(ans)
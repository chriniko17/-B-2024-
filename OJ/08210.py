l,n,m=map(int,input().split())
a=[0]
for i in range(n):
    a.append(int(input()))
a.append(l)
def rock(x):
    global m
    cur,num=0,0
    for i in range(1,n+2):
        if a[i]-cur<x:
            num+=1
        else:
            cur=a[i]
    if num>m:
        return True
    else:
        return False
left=0
right=l
ans=0
while left<right:
    mid=(left+right)//2
    if rock(mid):
        right=mid
    else:
        ans=mid
        left=mid+1
print(ans)
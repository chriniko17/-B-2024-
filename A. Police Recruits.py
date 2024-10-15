n=int(input())
a=list(map(int,input().split()))
p=0
ans=0
for i in range(n):
    if a[i]==-1 and p<=0:
        ans=ans+1
    elif a[i]==-1 and p>0:
        p=p-1
    else:
        p=p+a[i]
print(ans)
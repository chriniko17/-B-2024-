n,m=map(int,input().split())
a=list(map(int,input().split()))
mark={}
ans=[1]*n
for i in range(n-1,-1,-1):
    #print(set(a[i+1:n]))
    if a[i] not in mark:
        ans[i]=ans[i+1]+1 if i<n-1 else 1
    else:
        ans[i]=ans[i+1]
    mark[a[i]]=i
    #print(ans)
for i in range(m):
    l=int(input())
    print(ans[l-1])
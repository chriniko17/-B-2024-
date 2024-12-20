t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    m=list(map(int,input().split()))
    p=list(map(int,input().split()))
    ans=[p[i] for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if m[i]-m[j]<=k:
                break
            else:
                ans[i]=max(ans[i],ans[j]+p[i])
    print(max(ans))
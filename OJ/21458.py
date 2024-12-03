T,n=map(int,input().split())
ans=[float("-inf")]*(T+1)
ans[0]=0
for _ in range(n):
    t,w=map(int,input().split())
    for i in range(T,t-1,-1):
        ans[i]=max(ans[i],ans[i-t]+w)
if ans[T]==float("-inf"):
    print(-1)
else:
    print(ans[T])
n=int(input())
ans=[0]*101
for _ in range(n):
    a,b=map(int,input().split())
    ans[a],ans[a+1]=1,1
    for i in range(a+2,b+1):
        ans[i]=ans[i-1]+ans[i-2]
    print(ans[b])
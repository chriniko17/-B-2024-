n,b=map(int,input().split())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
ans=[0]*(b+1)
for i in range(n):
    for j in range(b,w[i]-1,-1):
        ans[j]=max(ans[j],ans[j-w[i]]+p[i])
    #print(ans)
print(ans[b])

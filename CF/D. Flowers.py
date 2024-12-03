t,k=map(int,input().split())
ans=[0]*(10**5+1)
presum=[0]*(10**5+1)
ans[0]=1
for i in range(1,k):
    ans[i]=1
    presum[i]=presum[i-1]+ans[i]
for i in range(k,10**5+1):
    ans[i]=(ans[i-1]+ans[i-k])%(10**9+7)
    presum[i]=(presum[i-1]+ans[i])%(10**9+7)
for _ in range(t):
    a,b=map(int,input().split())
    #print(ans[a:b+1],presum[a:b+1])
    print((presum[b]-presum[a-1])%(10**9+7))

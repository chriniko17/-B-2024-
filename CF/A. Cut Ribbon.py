n,a,b,c=map(int,input().split())
ans=[0]*(n+1)
for i in range(n+1):
    if i>=a and ans[i-a]!=0:
        ans[i]=max(ans[i],ans[i-a]+1)
    elif i==a:
        ans[i]=max(ans[i],1)
    if i>=b and ans[i-b]!=0:
        ans[i]=max(ans[i],ans[i-b]+1)
    elif i==b:
        ans[i]=max(ans[i],1)
    if i>=c and ans[i-c]!=0:
        ans[i]=max(ans[i],ans[i-c]+1)
    elif i==c:
        ans[i]=max(ans[i],1)
    #print(ans)
print(ans[n])
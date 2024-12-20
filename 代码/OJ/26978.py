n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=max(a[0:k])
print(ans,end=" ")
for i in range(n-k):
    if a[i+k]>ans:
        ans=a[i+k]
    elif a[i]==ans:
        ans=max(a[i+1:i+k+1])
    print(ans,end=" ")
ratings=[1,0,2]
n=len(ratings)
ans=[-1]*n
ans[0]=1
for i in range(1,n):
    if ratings[i]>ratings[i-1]:
        ans[i]=ans[i-1]+1
    else:
        ans[i]=1
suma=max(ans[n-1],1)
right=1
for i in range(n-2,-1,-1):
    if ratings[i]>ratings[i+1]:
        right+=1
    else:
        right=1
    suma+=max(ans[i],right)
print(suma)
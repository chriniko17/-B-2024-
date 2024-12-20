n=int(input())
ans=[0]*n
for i in range(n):
    a=list(map(int,input().split()))
    if i==0:
        ans[0]=a[0]
    else:
        temp=[0]*n
        temp[0]=ans[0]+a[0]
        temp[i]=ans[i-1]+a[i]
        for j in range(1,i):
            temp[j]=max(ans[j],ans[j-1])+a[j]
        ans=temp
        #print(ans)
print(max(ans))

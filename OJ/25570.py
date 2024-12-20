n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
ans=float("-inf")
for i in range((n+1)//2):
    temp=0
    if n%2==1 and i==(n-1)/2:
        temp=a[i][i]
    else:
        temp=sum(a[i][i:n-i])+sum(a[n-i-1][i:n-i])
        #print(a[i][i:n-i],a[n-i-1][i:n-i],temp)
        for j in range(i+1,n-i-1):
            temp+=a[j][i]+a[j][n-i-1]
            #print(a[j][i],a[j][n-i-1])
    ans=max(temp,ans)
print(ans)
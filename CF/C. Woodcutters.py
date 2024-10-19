a=[]
n=int(input())
for i in range(n):
    x,h=map(int,input().split())
    a.append([x,h])
ans=1
i=1
mark=0
while i<n-1:
    if a[i][0]-a[i-1][0]>a[i][1] and mark==0:
        ans+=1
        i+=1
    elif a[i+1][0]-a[i][0]>a[i][1]+a[i+1][1]:
        ans+=2
        i+=2
        mark=0
    elif a[i+1][0]-a[i][0]>a[i][1]:
        if a[i+1][0]-a[i][0]<=a[i+1][1]:
            ans+=1
            i+=1
            mark=0
        else:
            ans+=1
            mark=1
            i+=1
    else:
        i+=1
        mark=0
if i==n-1:
    print(ans+1)
else:
    print(ans)
n=int(input())
a=list(map(int,input().split()))
left=[1]*n
for i in range(1,n):
    if a[i]>a[i-1]:
        left[i]=left[i-1]+1
    else:
        left[i]=1
right=[1]*n
ans=left[n-1]
for i in range(n-2,-1,-1):
    if a[i]>a[i+1]:
        right[i]=right[i+1]+1
    else:
        right[i]=1
    ans+=max(right[i],left[i])
#print(right,left)
print(ans)



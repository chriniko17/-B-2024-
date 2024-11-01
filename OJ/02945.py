k=int(input())
a=list(map(int,input().split()))
ans=[1]*k
for i in range(k):
    for j in range(i):
        if a[j]>=a[i]:
            ans[i]=max(ans[i],ans[j]+1)
print(max(ans))
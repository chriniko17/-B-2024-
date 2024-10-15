n=int(input())
a=sorted(list(map(int,input().split())))
ans=1
for i in range(n):
    ans=max(ans,a.count(a[i]))
print(ans)
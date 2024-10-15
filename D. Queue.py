n=int(input())
a=sorted(list(map(int,input().split())))
time=0
ans=0
for i in range(n):
    if a[i]>=time:
        ans+=1
        time+=a[i]
    else:
        continue
print(ans)

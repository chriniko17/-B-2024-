n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]-=520
cur_sum=0
cur_map={0:-1}
ans=0
for i in range(n):
    cur_sum+=a[i]
    if cur_sum in cur_map:
        ans=max(ans,i-cur_map[cur_sum])
    else:
        cur_map[cur_sum]=i
print(ans*520)

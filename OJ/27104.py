import heapq
n=int(input())
a=list(map(int,input().split()))
ran=[]
for i in range(n):
    heapq.heappush(ran,(i-a[i],i+a[i]))
ans,end,cure=0,0,0
while ran:
    ans+=1
    left,right=heapq.heappop(ran)
    while left<=cure and ran:
        end=max(end,right)
        left,right=heapq.heappop(ran)
    cure=end
    if cure>=n-1:
        break
print(ans)
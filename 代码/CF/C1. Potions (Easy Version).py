import heapq

n=int(input())
a=list(map(int,input().split()))
ans=[]
blood=0
for i in range(n):
    if blood+a[i]>=0:
        blood+=a[i]
        heapq.heappush(ans,a[i])
    elif ans and a[i]>ans[0]:
        temp=heapq.heappop(ans)
        heapq.heappush(ans,a[i])
        blood+=a[i]-temp
print(len(ans))

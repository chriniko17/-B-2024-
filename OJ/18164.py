import heapq
n=int(input())
a=list(map(int,input().split()))
heapq.heapify(a)
ans=0
while len(a)>1:
    b=heapq.heappop(a)
    c=heapq.heappop(a)
    ans+=b+c
    heapq.heappush(a,b+c)
    #print(a)
print(ans)

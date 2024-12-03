import heapq

m,n,p=map(int,input().split())
a=[[float("inf")]*(n+2) for i in range(m+2)]
dir=[[0,1],[1,0],[0,-1],[-1,0]]
for i in range(m):
    s=list(input().split())
    for j in range(len(s)):
        if s[j]!="#":
            a[i+1][j+1]=int(s[j])
def dijkstra(x1,y1,x2,y2):
    pq=[(0,x1,y1)]
    dist=[[float("inf")]*(n+2) for i in range(m+2)]
    dist[x1][y1]=0
    while pq:
        cost,x,y=heapq.heappop(pq)
        if x==x2 and y==y2:
            return cost
        else:
            for i in range(4):
                nx,ny=x+dir[i][0],y+dir[i][1]
                if dist[nx][ny]>dist[x][y]+abs(a[nx][ny]-a[x][y]):
                    dist[nx][ny]=dist[x][y]+abs(a[nx][ny]-a[x][y])
                    heapq.heappush(pq,(cost+abs(a[nx][ny]-a[x][y]),nx,ny))
    return float("inf")
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    x1,y1,x2,y2=x1+1,y1+1,x2+1,y2+1
    if a[x1][y1]==float("inf") or a[x2][y2]==float("inf"):
        print("NO")
        continue
    ans=dijkstra(x1,y1,x2,y2)
    if ans==float("inf"):
        print("NO")
    else:
        print(ans)

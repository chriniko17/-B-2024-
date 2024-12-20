import heapq
n=int(input())
land=[]
dir=[[0,1],[0,-1],[1,0],[-1,0]]
for i in range(n):
    land.append(input())
visited=[[True]*(len(land[i])) for i in range(len(land))]
def find(x1,y1):
    pos=[]
    heapq.heappush(pos,(0,x1,y1))
    visited[x1][y1]=False
    while pos:
        step,x,y=heapq.heappop(pos)
        #print(step,x,y)
        if land[x][y]=="1" and step!=0:
            return step
        for dx,dy in dir:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<len(land[nx]) and visited[nx][ny]:
                visited[nx][ny]=False
                if land[nx][ny]==land[x][y] and land[x][y]!="0":
                    heapq.heappush(pos,(step,nx,ny))
                else:
                    heapq.heappush(pos,(step+1,nx,ny))
mark=False
for i in range(n):
    for j in range(len(land[i])):
        if land[i][j]=="1":
            print(find(i,j)-1)
            exit()




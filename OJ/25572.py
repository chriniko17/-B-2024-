from collections import deque
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
dir=[[0,1],[0,-1],[1,0],[-1,0]]
t=[[0,1],[1,0]]
visited=[[True]*n for i in range(n)]
sx,sy=-1,-1
ty=0
for i in range(n):
    for j in range(n):
        if a[i][j]==5:
            sx,sy=i,j
            if 0<=sx<n-1 and a[sx+1][sy]==5:
                ty=1
            break
    if sx!=-1:
        break
def find(x,y):
    global ty
    visit=deque([(x,y)])
    while visit:
        sx,sy=visit.popleft()
        #print(sx,sy,end="!")
        visited[sx][sy]=False
        x1,y1=sx+t[ty][0],sy+t[ty][1]
        if a[sx][sy]==9 or a[x1][y1]==9:
            return "yes"
        else:
            for dx,dy in dir:
                nx,ny=sx+dx,sy+dy
                #print(nx,ny)
                x2,y2=nx+t[ty][0],ny+t[ty][1]
                if 0<=nx<n and 0<=ny<n and a[nx][ny]!=1 and 0<=x2<n and 0<=y2<n and a[x2][y2]!=1 and visited[nx][ny]:
                    visit.append((nx,ny))
    return "no"
print(find(sx,sy))



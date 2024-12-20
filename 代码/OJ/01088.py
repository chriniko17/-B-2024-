r,c=map(int,input().split())
h=[list(map(int,input().split())) for i in range(r)]
length=[[float("-inf")]*c for i in range(r)]
dir=[[0,-1],[-1,0],[0,1],[1,0]]
def find(x,y):
    if length[x][y]!=float("-inf"):
        return length[x][y]
    ans=1
    for dx,dy in dir:
        nx,ny=x+dx,y+dy
        if 0<=nx<r and 0<=ny<c and h[nx][ny]<h[x][y]:
            ans=max(ans,find(nx,ny)+1)
    length[x][y]=ans
    return ans
a=1
for i in range(r):
    for j in range(c):
        a=max(a,find(i,j))
print(a)

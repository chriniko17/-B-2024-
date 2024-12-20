from collections import  deque
t=int(input())
dir=[[-1,0],[0,-1],[1,0],[0,1]]
for _ in range(t):
    r,c,k=map(int,input().split())
    a=[[0]*(c) for i in range(r)]
    x1,y1,x2,y2=0,0,0,0
    for i in range(r):
        s=input()
        for j in range(c):
            if s[j]=="S":
                x1,y1=i,j
            elif s[j]=="#":
                a[i][j]=1
            elif s[j]=="E":
                x2,y2=i,j
    visit=[[[True]*c for i in range(r)] for j in range(k)]
    def find(x1,y1,x2,y2,k):
        pos=deque([(0,x1,y1)])
        visit[0][x1][y1]=False
        while pos:
            t,i,j=pos.popleft()
            if i==x2 and j==y2:
                return t
            nt=t+1
            for di in dir:
                nx,ny=i+di[0],j+di[1]
                if 0<=nx<r and 0<=ny<c:
                    if a[nx][ny]==1 and nt%k!=0:
                        continue
                    if visit[nt%k][nx][ny]:
                        pos.append((nt,nx,ny))
                        visit[nt%k][nx][ny]=False
        return "Oop!"
    print(find(x1,y1,x2,y2,k))


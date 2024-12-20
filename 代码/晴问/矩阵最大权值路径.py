n,m=map(int,input().split())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
used=[[True]*m for i in range(n)]
used[0][0]=False
path=[[0,0]]
ans=a[0][0]
mark=float("-inf")
path1=[]
def find(i,j):
    global ans,mark,path1
    if i==n-1 and j==m-1:
        if ans>mark:
            path1=[path[i] for i in range(len(path))]
            mark=ans
        return
    if i-1>=0 and used[i-1][j]==True:
        ans+=a[i-1][j]
        used[i-1][j]=False
        path.append([i-1,j])
        find(i-1,j)
        used[i-1][j]=True
        ans-=a[i-1][j]
        path.pop(len(path)-1)
    if i+1<=n-1 and used[i+1][j]==True:
        ans+=a[i+1][j]
        used[i+1][j]=False
        path.append([i+1,j])
        find(i+1,j)
        used[i+1][j]=True
        path.pop(len(path)-1)
        ans-=a[i+1][j]
    if j-1>=0 and used[i][j-1]==True:
        ans+=a[i][j-1]
        used[i][j-1]=False
        path.append([i,j-1])
        find(i,j-1)
        used[i][j-1]=True
        path.pop(len(path)-1)
        ans-=a[i][j-1]
    if j+1<=m-1 and used[i][j+1]==True:
        ans+=a[i][j+1]
        used[i][j+1]=False
        path.append([i,j+1])
        find(i,j+1)
        used[i][j+1]=True
        path.pop(len(path)-1)
        ans-=a[i][j+1]
find(0,0)
for i in range(len(path1)):
    print(path1[i][0]+1,path1[i][1]+1)
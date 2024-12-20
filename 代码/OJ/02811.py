a=[list(map(int,input().split())) for i in range(5)]
record=[]
for i in range(5):
    temp=[]
    for j in range(6):
        temp.append(a[i][j])
    record.append(temp)
man=[[0]*6 for i in range(5)]
dir=[[0,0],[0,1],[1,0],[0,-1],[-1,0]]
def do(x,y):
    man[x][y]=1
    for dx,dy in dir:
        nx,ny=x+dx,y+dy
        if 0<=nx<5 and 0<=ny<6:
            if a[nx][ny]==0:
                a[nx][ny]=1
            else:
                a[nx][ny]=0
def make(n):
    ans=[]
    temp=[]
    def inmake(i):
        #print(i,temp)
        if i==n:
            temp1=[temp[i] for i in range(len(temp))]
            ans.append(temp1)
            return
        else:
            for j in range(2):
                temp.append(j)
                inmake(i+1)
                temp.pop()
    inmake(0)
    return ans
perm=make(6)
for element in perm:
    for i in range(6):
        if element[i]==1:
            do(0,i)
    for i in range(4):
        for j in range(6):
            if a[i][j]==1:
                do(i+1,j)
    if a[4].count(1)==0:
        for i in range(5):
            print(" ".join(map(str,man[i])))
        break
    else:
        man=[[0]*6 for i in range(5)]
        for i in range(5):
            for j in range(6):
                a[i][j]=record[i][j]
t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    a=[[True]*m for i in range(n)]
    mark=1
    ans=0
    a[x][y]=False
    def find(i,j):
        global a,mark,ans,n,m
        #print(mark,ans,i,j,a,n,m)
        if mark==n*m:
            ans+=1
            return
        else:
            if i-2>=0 and j-1>=0 and a[i-2][j-1]==True:
                mark+=1
                a[i-2][j-1]=False
                find(i-2,j-1)
                a[i-2][j-1]=True
                mark-=1
            if i-2>=0 and j+1<=m-1 and a[i-2][j+1]==True:
                mark+=1
                a[i-2][j+1]=False
                find(i-2,j+1)
                a[i-2][j+1]=True
                mark-=1
            if i-1>=0 and j-2>=0 and a[i-1][j-2]==True:
                mark+=1
                a[i-1][j-2]=False
                find(i-1,j-2)
                a[i-1][j-2]=True
                mark-=1
            if i-1>=0 and j+2<=m-1 and a[i-1][j+2]==True:
                mark+=1
                a[i-1][j+2]=False
                find(i-1,j+2)
                a[i-1][j+2]=True
                mark-=1
            if i+2<=n-1 and j-1>=0 and a[i+2][j-1]==True:
                mark+=1
                a[i+2][j-1]=False
                find(i+2,j-1)
                a[i+2][j-1]=True
                mark-=1
            if i+2<=n-1 and j+1<=m-1 and a[i+2][j+1]==True:
                mark+=1
                a[i+2][j+1]=False
                find(i+2,j+1)
                a[i+2][j+1]=True
                mark-=1
            if i+1<=n-1 and j-2>=0 and a[i+1][j-2]==True:
                mark+=1
                a[i+1][j-2]=False
                find(i+1,j-2)
                a[i+1][j-2]=True
                mark-=1
            if i+1<=n-1 and j+2<=m-1 and a[i+1][j+2]==True:
                mark+=1
                a[i+1][j+2]=False
                find(i+1,j+2)
                a[i+1][j+2]=True
                mark-=1
    find(x,y)
    print(ans)
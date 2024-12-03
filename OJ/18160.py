import sys
sys.setrecursionlimit(3000000)
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        a.append(input())
    pond=[[0]*m for i in range(n)]
    mid=0
    def find(i,j):
        global mid
        pond[i][j]=1
        mid+=1
        if i>0:
            if a[i-1][j]=="W" and pond[i-1][j]==0:
                find(i-1,j)
            if j>0:
                if a[i-1][j-1] == "W" and pond[i-1][j-1] == 0:
                    find(i-1, j-1)
            if j<m-1:
                if a[i-1][j+1] == "W" and pond[i-1][j+1] == 0:
                    find(i - 1, j+1)
        if j > 0:
            if a[i][j-1] == "W" and pond[i][j-1] == 0:
                find(i, j-1)
        if j < m - 1:
            if a[i][j + 1] == "W" and pond[i][j + 1] == 0:
                find(i, j + 1)
        if i<n-1:
            if a[i+1][j]=="W" and pond[i+1][j]==0:
                find(i+1,j)
            if j>0:
                if a[i + 1][j-1] == "W" and pond[i +1][j-1] == 0:
                    find(i + 1, j-1)
            if j<m-1:
                if a[i + 1][j+1] == "W" and pond[i + 1][j+1] == 0:
                    find(i +1, j+1)
    ans=0
    for i in range(n):
        for j in range(m):
            if a[i][j]=="W" and pond[i][j]==0:
                mid=0
                find(i,j)
                ans=max(ans,mid)
    print(ans)
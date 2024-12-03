n,m=map(int,input().split())
a=[]
marki,markj=-1,-1
for i in range(n):
    temp=list(map(int,input().split()))
    a.append(temp)
    if 1 in set(temp):
        marki=i
        markj=temp.index(1)
ans=[[float("inf")]*m for i in range(n)]
ans[0][0]=0
def find(i,j):
    if i>0:
        if a[i-1][j]!=2 and ans[i-1][j]>ans[i][j]+1:
            ans[i-1][j]=ans[i][j]+1
            find(i-1,j)
    if i<n-1:
        if a[i+1][j]!=2 and ans[i+1][j]>ans[i][j]+1:
            ans[i+1][j]=ans[i][j]+1
            find(i+1,j)
    if j>0:
        if a[i][j-1]!=2 and ans[i][j-1]>ans[i][j]+1:
            ans[i][j-1]=ans[i][j]+1
            find(i,j-1)
    if j<m-1:
        if a[i][j+1]!=2 and ans[i][j+1]>ans[i][j]+1:
            ans[i][j+1]=ans[i][j]+1
            find(i,j+1)
find(0,0)
if ans[marki][markj]==float("inf"):
    print("NO")
else:
    print(ans[marki][markj])
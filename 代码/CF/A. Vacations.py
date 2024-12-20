from bisect import insort_right

n=int(input())
a=list(map(int,input().split()))
ans=[[0]*3 for i in range(n)]
ans[0][0]=1
if a[0]==0:
    ans[0][1]=ans[0][2]=float("inf")
elif a[0]==1:
    ans[0][1]=float("inf")
    ans[0][2]=0
elif a[0]==2:
    ans[0][1]=0
    ans[0][2]=float("inf")
else:
    ans[0][1]=ans[0][2]=0
for i in range(1,n):
    ans[i][0]=min(ans[i-1])+1
    if a[i]==0:
        ans[i][1]=ans[i][2]=float("inf")
    elif a[i]==1:
        ans[i][1]=float("inf")
        ans[i][2]=min(ans[i-1][0],ans[i-1][1])
    elif a[i]==2:
        ans[i][2] = float("inf")
        ans[i][1] = min(ans[i - 1][0], ans[i - 1][2])
    elif a[i]==3:
        ans[i][1] = min(ans[i - 1][0], ans[i - 1][2])
        ans[i][2] = min(ans[i - 1][0], ans[i - 1][1])
print(min(ans[n-1]))
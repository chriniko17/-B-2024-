n=int(input())
ans=[float("-inf")]*3
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans[1],ans[2]=a[0],b[0]
for i in range(1,n):
    ans[0],ans[1],ans[2]=max(ans),max(ans[0],ans[2])+a[i],max(ans[0],ans[1])+b[i]
print(max(ans))

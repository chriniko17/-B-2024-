from bisect import bisect_left

t=int(input())
for _ in range(t):
    n=int(input())
    temp=list(map(int,input().split()))
    a=[]
    for i in range(n):
        a.append(temp[i*2:i*2+2])
    a.sort()
    a.sort(reverse=True)
    #print(a)
    ans=[]
    for i in range(n):
        pos=bisect_left(ans,a[i][1])
        if pos==len(ans):
            ans.append(a[i][1])
        else:
            ans[pos]=a[i][1]
    #print(ans)
    print(len(ans))

from bisect import bisect_left

n=int(input())
a=list(map(int,input().split()))
a.reverse()
ans=[]
for num in a:
    pos=bisect_left(ans,num)
    if len(ans)==pos:
       ans.append(num)
    else:
        ans[pos]=num
print(len(ans))
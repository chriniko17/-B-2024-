import math
n=int(input())
x,y=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
a.sort(key=lambda x:x[0]*x[1])
#print(a)
ans,cur=0,x
for i in range(n):
    #print(cur/a[i][1])
    ans=max(ans,(cur//a[i][1]))
    cur*=a[i][0]
print(ans)
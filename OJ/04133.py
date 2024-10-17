c=[[0]*1025 for i in range(1025)]
d=int(input())
n=int(input())
num,ans=1,0
for _ in range(n):
    x,y,m=map(int,input().split())
    for i in range(max(0,x-d),min(1025,x+d+1)):
        for j in range(max(0,y-d),min(1025,y+d+1)):
            c[i][j]+=m
for i in range(1025):
    for j in range(1025):
        if c[i][j]>ans:
            num=1
            ans=c[i][j]
        elif c[i][j]==ans:
            num+=1
print(num,ans)
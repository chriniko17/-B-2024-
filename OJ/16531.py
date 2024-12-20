m,n=map(int,input().split())
pos=[list(map(int,input().split())) for i in range(m)]
pro=[list(map(int,input().split())) for i in range(n*m)]
dir=[[0,-1],[-1,0],[1,0],[0,1]]
count=0
dic={}
for i in range(m):
    for j in range(n):
        s=sum(pro[pos[i][j]])
        if s not in dic:
            dic[s]=1
        else:
            dic[s]+=1
        for dx,dy in dir:
            ni,nj=i+dx,j+dy
            if 0<=ni<m and 0<=nj<n and pro[pos[i][j]]==pro[pos[ni][nj]]:
                count+=1
                break
people=0
for key in sorted(list(dic.keys()),reverse=True):
    if people+dic[key]<=m*n*0.4:
        people+=dic[key]
    else:
        break
print(count,people)


a,b,m=map(int,input().split())
d=[[-1]*b for i in range(a)]
k=0
for q in range(m):
    r,s,p,t=map(int,input().split())
    r-=1
    s-=1
    if t==0:
        for i in range(max(0,r-(p-1)//2),min(a,r+(p-1)//2+1)):
            for j in range(max(0,s-(p-1)//2),min(b,s+(p-1)//2+1)):
                d[i][j]=0
    else:
        for i in range(max(0,r-(p-1)//2),min(a,r+(p-1)//2+1)):
            for j in range(max(0,s-(p-1)//2),min(b,s+(p-1)//2+1)):
                if d[i][j]!=0:
                    d[i][j]+=2
        k+=1
    #print(d)
ans=0
mark=-1+2*k
for i in range(a):
    for j in range(b):
        if d[i][j]==mark:
            ans+=1
print(ans)
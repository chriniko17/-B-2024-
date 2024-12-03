import sys
origin=sys.stdin.read()
sys.setrecursionlimit(30000000)
data=origin.split()
ind=1
k=int(data[0])
dire=[[0,1],[1,0],[0,-1],[-1,0]]
result=[]
for _ in range(k):
    m,n=map(int,data[ind:ind+2])
    ind+=2
    h=[]
    water=[[-1]*n for i in range(m)]
    for _ in range(m):
        h.append(list(map(int,data[ind:ind+n])))
        ind+=n
    I,J=map(int,data[ind:ind+2])
    ind+=2
    p=int(data[ind])
    ind+=1
    def find(i,j,m,n,hw):
        #print(i,j)
        water[i][j]=hw
        for k in range(4):
            x,y=i+dire[k][0],j+dire[k][1]
            if x>=0 and x<m and y>=0 and y<n and h[x][y]<=hw and water[x][y]<hw:
                find(x,y,m,n,hw)
    for _ in range(p):
        x,y=map(int,data[ind:ind+2])
        ind+=2
        if h[x-1][y-1]>water[x-1][y-1]:
            find(x-1,y-1,m,n,h[x-1][y-1])
    #print(water)
    result.append("No" if h[I-1][J-1]>=water[I-1][J-1] else "Yes")
sys.stdout.write("\n".join(result)+ "\n")
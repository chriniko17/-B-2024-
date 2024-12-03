import sys
sys.setrecursionlimit(3000000)
mark=0
dire=[[0,1],[1,0],[0,-1],[-1,0]]
while True:
    result=[]
    mark+=1
    w,h=map(int,input().split())
    if w+h==0:
        break
    a=[[0]*(w+2) for i in range(h+2)]
    for i in range(1,h+1):
        s=input()
        for j in range(1,w+1):
            if s[j-1]=="X":
                a[i][j]=1
    while True:
        visit=[[False]*(w+2) for i in range(h+2)]
        x1,y1,x2,y2=map(int,input().split())
        if x1+y1+x2+y2==0:
            break
        a[y1][x1],a[y2][x2]=0,0
        dp=[[float("inf")]*(w+2) for i in range(h+2)]
        def find(i,j,mark,turn):
            #print(i,j,mark,turn)
            if dp[j][i]<=turn:
                return float("inf")
            dp[j][i]=turn
            if i==x2 and j==y2:
                return turn
            mim=float("inf")
            for k in range(4):
                cx,cy=i+dire[k][0],j+dire[k][1]
                if cx>=0 and cx<=w+1 and cy>=0 and cy<=h+1 and visit[cy][cx]==False and a[cy][cx]==0:
                    visit[cy][cx]=True
                    new_turn=turn+1 if k!=mark else turn
                    result=find(cx,cy,k,new_turn)
                    mim=min(mim,result)
                    visit[cy][cx]=False
            return mim
        visit[y1][x1]=True
        result.append(find(x1,y1,-1,0))
        #print(find(x1,y1,-1,0))
        a[y1][x1],a[y2][x2]=1,1
    print("Board #"+str(mark)+":")
    for i in range(len(result)):
        print("Pair "+str(i+1)+": ",end="")
        if result[i]==float("inf"):
            print("impossible.")
        else:
            print(str(result[i])+" segments.")
    print()
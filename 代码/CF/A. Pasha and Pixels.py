n,m,k=map(int,input().split())
a=[([0]*(m+2)) for i in range(n+2)]
#print(a)
for i in range(k):
    x,y=map(int,input().split())
    a[x][y]=1
    if a[x-1][y]==1 and a[x][y-1]==1 and a[x-1][y-1]==1:
        print(i+1)
        exit()
    elif a[x-1][y]==1 and a[x-1][y+1]==1 and a[x][y+1]==1:
        print(i+1)
        exit()
    elif a[x+1][y]==1 and a[x][y-1]==1 and a[x+1][y-1]==1:
        print(i+1)
        exit()
    elif a[x+1][y]==1 and a[x][y+1]==1 and a[x+1][y+1]==1:
        print(i+1)
        exit()
print(0)

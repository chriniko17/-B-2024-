n,k=map(int,input().split())
a=[["0"]*n for i in range(n)]
if k>n**2:
    print(-1)
    exit()
if k==1:
    a[0][0]="1"
    k-=1
for i in range(n):
    for j in range(i,n):
        #print(k)
        if k<=1:
            break
        else:
            if j==i:
                a[i][i]="1"
                k-=1
            else:
                a[i][j]="1"
                a[j][i]="1"
                k-=2
    if k==1:
        a[i+1][i+1]="1"
        break
    elif k==0:
        break
for i in range(n):
    print(" ".join(a[i]))

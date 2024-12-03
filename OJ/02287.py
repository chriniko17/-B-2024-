while True:
    n=int(input())
    if n==0:
        break
    a=sorted(list(map(int,input().split())))
    b=sorted(list(map(int,input().split())))
    pre=[0]*(n+1)
    for i in range(n-1,-1,-1):
        for j in range(n):
            if a[i]<b[j]:
                pre[j]=-1+pre[j]
            elif a[i]>b[j]:
                pre[j]=1+pre[j+1]
            else:
                pre[j]=max(-1+pre[j],pre[j+1])
    print(pre[0]*200)

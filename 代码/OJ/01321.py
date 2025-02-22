while True:
    n,k=map(int,input().split())
    if n+k==-2:
        break
    a=[]
    ans=0
    for _ in range(n):
        a.append(input())
    row=[]
    def find(n,k,i,y):
        global ans
        if i==k+1:
            ans+=1
            return
        if y>=n:
            return
        for j in range(y,n):
            for m in range(n):
                if a[j][m]=="#" and m not in set(row):
                    row.append(m)
                    find(n,k,i+1,j+1)
                    row.pop()
    find(n,k,1,0)
    print(ans)

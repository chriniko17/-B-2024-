t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    if sum(a)%x!=0:
        print(n)
    else:
        left,right=-1,-1
        for i in range(n):
            if a[i]%x!=0:
                left=i
                break
        for i in range(n-1,-1,-1):
            if a[i]%x!=0:
                right=i
                break
        if left+right==-2:
            print(-1)
        else:
            print(max(n-left-1,right))
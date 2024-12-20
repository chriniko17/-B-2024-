t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(list(map(int,input().split())))
    for k in range(n,-1,-1):
        i,j,bod=0,n-1,k
        while a[j]>bod and j>=0:
            j-=1
        while i<=j:
            j-=1
            i+=1
            bod-=1
            while a[j]>bod and j>=0:
                j-=1
        if i>=k:
            print(k)
            break
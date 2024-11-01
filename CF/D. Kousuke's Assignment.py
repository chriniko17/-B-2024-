t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    suma=0
    prefix={0:-1}
    ans=0
    mark=-1
    for i in range(n):
        suma+=a[i]
        if suma in prefix and prefix[suma]>=mark:
            ans+=1
            mark=i
        prefix[suma]=i
    print(ans)


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    suma=0
    prefix=set()
    ans=0
    for i in range(n):
        suma+=a[i]
        if suma==0 or suma in prefix:
            ans+=1
            suma=0
            prefix.clear()
        else:
            prefix.add(suma)
    print(ans)

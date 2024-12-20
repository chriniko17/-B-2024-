t=int(input())
for _ in range(t):
    n=int(input())
    ans=0
    while n>0:
        if n==4:
            ans+=3
            n=0
        elif n%2==1:
            ans+=1
            n=n//2
        elif n%4==0:
            ans+=1
            n-=2
        else:
            ans+=n//2
            n=n//2-1
    print(ans)
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=set()
    a.add(m)
    while True:
        b=list(a)
        if n in a:
            print("yes")
            break
        if min(a)>n:
            print("no")
            break
        for i in range(len(b)):
            a.add(b[i]*3)
            if b[i]%2==0:
                a.add(int(b[i]/2*3))
            a.remove(b[i])

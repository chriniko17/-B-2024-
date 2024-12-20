n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
s=sum(a)
while True:
    if a[-1]>s/k:
        s-=a.pop()
        k-=1
    else:
        print("{:.3f}".format(s/k))
        break
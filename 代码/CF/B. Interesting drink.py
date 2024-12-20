n=int(input())
a=sorted(list(map(int,input().split())))
mark=[0 for i in range(100001)]
for i in range(n-1):
    for j in range(a[i],a[i+1]):
        mark[j]=i+1
q=int(input())
for _ in range(q):
    m=int(input())
    if m>=a[n-1]:
        print(n)
    else:
        print(mark[m])
q=int(input())
for _ in range(q):
    n=int(input())
    a=sorted(map(int,input().split()))
    ans=0
    for i in range(n):
        if a[i]>2048:
            break
        else:
            ans+=a[i]
    if ans>=2048:
        print("YES")
    else:
        print("NO")
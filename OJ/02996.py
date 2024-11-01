def do(a):
    mark=-1
    for i in range(len(a)-2,-1,-1):
        if a[i]<a[i+1]:
            mark=i
            break
    if mark==-1:
        a.sort()
    else:
        for i in range(len(a)-1,mark,-1):
            if a[i]>a[mark]:
                a[i],a[mark]=a[mark],a[i]
                break
        a[mark+1::]=a[mark+1::][::-1]
n=int(input())
m=int(input())
a=list(map(int,input().split()))
for i in range(m):
    do(a)
print(" ".join(map(str,a)))
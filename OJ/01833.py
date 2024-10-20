import math
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(k%math.factorial(n)):
        mark = -1
        for i in range(n - 2, -1, -1):
            if a[i] < a[i + 1]:
                mark = i
                break
        #print(mark)
        if mark==-1:
            a.sort()
        else:
            for i in range(n-1,mark,-1):
                if a[i]>a[mark]:
                    a[i],a[mark]=a[mark],a[i]
                    break
            a[mark+1::]=a[mark+1::][::-1]
        #print(a)
    print(" ".join(map(str,a)))
import math
n=int(input())
used=[True]*(n+1)
ans=[0]*(n+1)
count=0
def find(x):
    global count
    if x==n+1:
        count+=1
        print(" ".join(map(str,ans[1:n+1])),end="")
        if count!=math.factorial(n):
            print()
    else:
        for i in range(1,n+1):
            if used[i]:
                ans[x]=i
                used[i]=False
                find(x+1)
                used[i]=True
find(1)
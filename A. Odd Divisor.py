import math
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if bin(a[i])[2:].count("1")!=1:
        print("YES")
    else:print("NO")

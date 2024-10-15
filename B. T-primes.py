m=1000000
a=[i for i in range(m+1)]
for i in range(2,int(m**0.5)+1):
    if a[i]!=0:
        k=i
        while k+i<=m:
            k+=i
            a[k]=0
s=set(a)
s.remove(0)
s.remove(1)
n=int(input())
b=list(map(int,input().split()))
for j in range(n):
    if b[j]**0.5!=int(b[j]**0.5):
        print("NO")
    elif int(b[j]**0.5) in s:
        print("YES")
    else:
        print("NO")
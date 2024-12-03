n,k,d=map(int,input().split())
a=[0]*(n+1)
a[0]=1
b=[0]*(n+1)
b[0]=1
for i in range(1,n+1):
    for j in range(1,k+1):
        if i>=j:
            a[i]+=a[i-j]
        else:
            break
    for j in range(1,d):
        if i>=j:
            b[i]+=b[i-j]
        else:
            break
print((a[n]-b[n])%(10**9+7))

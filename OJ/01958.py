a=[float("inf")]*13
a[1]=1
print(1)
for n in range(2,13):
    for k in range(1,n+1):
        a[n]=min(a[n],a[n-k]*2+2**k-1)
    print(a[n])
n=int(input())
a=[0]*n
if n==1:
    print(1)
else:
    a[0],a[1]=1,2
    for i in range(2,n):
        a[i]=a[i-1]+a[i-2]
    print(a[n-1])
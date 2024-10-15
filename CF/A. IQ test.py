n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]=a[i]%2
k=0
if a.count(1)==1:
    k=1
print(a.index(k)+1)

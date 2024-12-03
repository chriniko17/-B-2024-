def find(a):
    current=0
    total=float("-inf")
    for val in a:
        current+=val
        total=max(total,current)
        if current<0:
            current=0
    return total
n=int(input())
a=[]
ans=float("-inf")
while len(a)<n*n:
    a.extend(input().split())
a=list(map(int,a))
#print(a)
for i in range(n+1):
    for j in range(i):
        suma=[sum(a[j+n*k:i+n*k]) for k in range(n)]
        ans=max(ans,find(suma))
print(ans)
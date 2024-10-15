n=int(input())
a=list(input().split())
a.sort()
lmax=max(len(a[i]) for i in range(n))
c=[]
for i in range(n):
    temp=a[i]*int(lmax/len(a[i])+1)
    c.append([a[i],temp[0:lmax:]])
c.sort(key=lambda x:x[1])
#print(c)
b=c[::-1]
for i in range(n):
    print(b[i][0],end="")
print(" ",end="")
for i in range(n):
    print(c[i][0],end="")
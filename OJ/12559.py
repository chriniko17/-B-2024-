def make(x):
    if x==0:
        return 9
    else:
        return 9*10**x+make(x-1)
n=int(input())
a=list(input().split())
c=[]
for i in range(n):
    c.append([a[i],int(a[i])/make(len(a[i])-1)])
c.sort(key=lambda x:x[1])
b=c[::-1]
for i in range(n):
    print(b[i][0],end="")
print(" ",end="")
for i in range(n):
    print(c[i][0],end="")
n=int(input())
a=list(input().split())
a.sort()
print(a)
b=a[::-1]
for i in range(n):
    print(b[i],end="")
print(" ",end="")
for i in range(n):
    print(a[i],end="")
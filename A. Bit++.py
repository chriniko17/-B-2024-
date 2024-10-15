n=int(input())
x=0
for _ in range(n):
    op=input()
    if op.count("+")>0:
        x+=1
    else:
        x-=1
print(x)
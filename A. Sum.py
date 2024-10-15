n=int(input())
list=[]
for i in range(n):
    a,b,c=map(int,input().split())
    if a==b+c or b==a+c or c==a+b:
        list.append(1)
    else:list.append(0)
for i in range(n):
    if list[i]==1:
        print("YES")
    else:print("NO")
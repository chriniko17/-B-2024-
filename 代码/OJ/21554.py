n=int(input())
a=list(map(int,input().split()))
stu=[]
for i in range(n):
    stu.append([a[i],i+1])
stu.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    print(stu[i][1],end=" ")
print()
ans=0
for i in range(n):
    ans+=stu[i][0]*(n-i-1)
print("{:.2f}".format(ans/n))
n=int(input())
v=list(map(int,input().split()))
v2=sorted(v)
sum1=[0]
sum2=[0]
for i in range(n):
    sum1.append(sum1[i]+v[i])
    sum2.append(sum2[i]+v2[i])
#print(sum1,sum2)
m=int(input())
for _ in range(m):
    ty,l,r=map(int,input().split())
    if ty==1:
        print(sum1[r]-sum1[l-1])
    if ty==2:
        print(sum2[r]-sum2[l-1])
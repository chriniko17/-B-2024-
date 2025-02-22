from collections import deque
s=deque([])
n=int(input())
a=list(map(int,input().split()))
mark=0
for i in range(1,n+1):
    deque.append(s,i)
    while len(s)>0 and s[-1]==a[mark]:
        deque.pop(s)
        mark+=1
if len(s)==0:
    print("Yes")
else:
    print("No")
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    t1=0
    c=[]
    for i in range(n):
        if b[i]>=a[i]:
            t1=max(t1,a[i])
        else:
            c.append([a[i],b[i]])
    c.sort(key=lambda x:x[0],reverse=True)
    #print(c,t1)
    used=0
    t2=0
    c.append([-1,-1])
    for i in range(len(c)-1):
        if used+c[i][1]<=c[i+1][0]:
            used+=c[i][1]
        else:
            t2=max(t2,min(used+c[i][1],c[i][0]))
    print(max(t1,t2))
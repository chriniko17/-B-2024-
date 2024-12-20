k=1
while True:
    n,d=map(int,input().split())
    if n==d==0:
        break
    a=[]
    suc=False
    for _ in range(n):
        x,y=map(int,input().split())
        a.append([x-(d**2-y**2)**0.5,x+(d**2-y**2)**0.5])
        if y>d:
            suc=True
    blank=input()
    if suc or d<0:
        print("Case "+str(k)+": -1")
        k+=1
        continue
    a.sort(key=lambda x:x[1])
    r=a[0][1]
    ans=1
    for i in range(1,n):
        if r<a[i][0]:
            r=a[i][1]
            ans+=1
    print("Case "+str(k)+": "+str(ans))
    k+=1
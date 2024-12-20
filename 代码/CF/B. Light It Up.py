n,m=map(int,input().split())
a=list(map(int,input().split()))
inv=[0 for i in range(n+1)]
inv[0]=a[0]
for i in range(1,n):
    inv[i]=a[i]-a[i-1]
inv[n]=m-a[n-1]
timetot=[0 for i in range(n+1)]
timetot[n],timetot[n-1]=inv[n],inv[n-1]
for i in range(n-2,-1,-1):
    timetot[i]=timetot[i+2]+inv[i]
#print(timetot,inv)
ans=timetot[0]
for i in range(n+1):
    if i%2==0 and inv[i]>1:
        bt=timetot[0]-timetot[i]
        it=inv[i]-1
        if i==n:
            at=0
        else:
            at=timetot[i+1]
        ans=max(ans,bt+it+at)
    elif i%2==1 and inv[i]>1:
        if i==n:
            bt=timetot[0]
        else:
            bt=timetot[0]-timetot[i+1]
        it=inv[i]-1
        if i==n or i==n-1:
            at=0
        else:
            at=timetot[i+2]
        ans=max(ans,bt+it+at)
        #print(bt,it,at)
print(ans)
n=int(input())
a=list(map(int,input().split()))
tot=sum(a)/3
ansl,ansr=0,0
ans=0
setl=set()
setr=set()
for i in range(n):
    ansl+=a[i]
    if ansl==tot:
        setl.add(i)
for i in range(n-1,-1,-1):
    ansr+=a[i]
    if ansr==tot:
        setr.add(i)
setl=sorted(list(setl))
setr=sorted(list(setr))
#print(setl,setr)
if len(setl)==0 or len(setr)==0:
    print(0)
else:
    i,j=0,0
    while i<len(setl) and j<len(setr):
        if setl[i]<setr[j]-1:
            ans+=len(setr)-j
            i+=1
            #print(i,j)
        else:
            j+=1
    print(ans)
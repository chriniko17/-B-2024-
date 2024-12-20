t=int(input())
for _ in range(t):
    n=int(input())
    curlen=0
    i=0
    while n>=0:
        i+=1
        curlen+=len(str(i))
        n-=curlen
    i-=1
    n+=curlen
    if n==0:
        n=n+curlen-len(str(i))
        i-=1
    len1=0
    j=1
    while n>len1:
        n-=len1
        len1=len(str(j))
        j+=1
    print(str(j-1)[n-1])

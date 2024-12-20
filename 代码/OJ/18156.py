t=int(input())
a=sorted(list(map(int,input().split())))
i,j=0,len(a)-1
mim=float("inf")
ans=0
while i<j:
    suma=a[i]+a[j]
    if suma==t:
        print(t)
        exit()
    elif suma<t:
        i+=1
    else:
        j-=1
    if abs(t-suma)<mim or (abs(t-suma)==mim and suma<ans):
        mim=abs(t-suma)
        ans=suma
print(ans)
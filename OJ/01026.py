def findcir(a):
    ans=[]
    for i in range(len(a)):
        cir=1
        x=a[i]-1
        while x!=i:
            x=a[x]-1
            cir+=1
        ans.append(cir)
    return ans
while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    cir=findcir(a)
    while True:
        temp=input()
        if temp=="0":
            break
        k,op=temp.split(" ",1)
        k=int(k)
        op=list(op)
        if k==0:
            break
        while len(op)<n:
            op.append(" ")
        c=[" "]*n
        for i in range(n):
            x=i
            for j in range(k%cir[i]):
                x=a[x]-1
            c[x]=op[i]
        print("".join(c))
    print()


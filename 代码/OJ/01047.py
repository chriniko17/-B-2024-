def judge(a,b):
    if len(a)!=len(b) or a[0] not in set(b):
        return False
    else:
        n=len(a)
        for k in range(n):
            c=a[k::]+a[0:k:]
            if c==b:
                return True
        return False
try:
    while True:
        n=input()
        num=int(n)
        n=list(n)
        l=len(n)
        mark=0
        for i in range(2,l+1):
            b=list(str(num*i))[::-1]
            while len(b)<l:
                b.append("0")
            b=b[::-1]
            if not judge(n,b):
                print("".join(n)+" is not cyclic")
                mark=1
                break
        if mark==0:
            print("".join(n)+" is cyclic")
except EOFError:
    exit()
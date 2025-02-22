def check(x,i):
    s=bin(x)[2::][::-1]
    #print(s)
    if len(s)<i+1:
        return 0
    return 0 if s[i]=="0" else 1
n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    s=input()
    if s[0]=="C":
        num=int(s[2::])
        for j in range(n):
            a[j]=(a[j]+num)%65536
    else:
        num=int(s[2::])
        count=0
        for j in range(n):
            count+=check(a[j],num)
        print(count)
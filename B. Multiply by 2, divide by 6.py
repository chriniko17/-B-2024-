n=int(input())
for _ in range(n):
    a=int(input())
    if a==1:
        print("0")
    else:
        n=0;m=0
        while a%2==0:
            a/=2
            n+=1
        while a%3==0:
            a/=3
            m+=1
        if a!=1:
            print("-1")
        elif n>m:
            print("-1")
        else:
            print(m+m-n)
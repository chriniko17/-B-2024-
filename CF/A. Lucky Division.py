def judge(x):
    a=str(x)
    if len(a)-a.count("4")-a.count("7")==0:
        return 1
    else:
        return 0
n=int(input())
if judge(n)==1:
    print("YES")
    exit()
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0 and (judge(i)==1 or judge(int(n/i))==1):
            print("YES")
            exit()
    print("NO")
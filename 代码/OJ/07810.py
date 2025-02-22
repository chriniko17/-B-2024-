def judge(x):
    x=str(x)
    for i in range(len(x)-1):
        if x[i]=="1" and x[i+1]=="9":
            return True
    return False
n=int(input())
for _ in range(n):
    p=int(input())
    if judge(p) or p%19==0:
        print("Yes")
    else:
        print("No")

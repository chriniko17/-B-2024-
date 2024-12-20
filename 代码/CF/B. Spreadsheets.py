def trans1(x):
    x=x[::-1]
    ans=0
    for i in range(len(x)):
        ans+=(ord(x[i])-64)*(26**(i))
    return ans
def trans2(y):
    ans=[]
    while y>0:
        ans.append(chr((y-1)%26+65))
        y=(y-1)//26
    return ans[::-1]
n=int(input())
for _ in range(n):
    x=input()
    if x[0]=="R" and ord(x[1])<64 and "C" in x:
        mark=x.index("C")
        row=int(x[1:mark])
        col=int(x[mark+1:])
        print("".join(trans2(col))+str(row))
    else:
        mark=0
        for i in range(len(x)):
            if ord(x[i])<=64:
                mark=i
                break
        row=x[mark:]
        col=x[0:mark]
        print("R"+row+"C"+str(trans1(col)))

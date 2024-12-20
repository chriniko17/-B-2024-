a=list(input().split())
#print(a)
def judge(x):
    if x=="+" or x=="-" or x=="*" or x=="/":
        return -1
    else:
        return float(x)
while len(a)>1:
    for i in range(len(a)-1,-1,-1):
        if judge(a[i])==-1:
            temp=0
            if a[i]=="+":
                temp=judge(a[i+1])+judge(a[i+2])
            if a[i]=="-":
                temp=judge(a[i+1])-judge(a[i+2])
            if a[i]=="*":
                temp=judge(a[i+1])*judge(a[i+2])
            if a[i]=="/":
                temp=judge(a[i+1])/judge(a[i+2])
            a.pop(i+2)
            a.pop(i+1)
            a[i]=str(temp)
print("{:.6f}".format(float(a[0])))
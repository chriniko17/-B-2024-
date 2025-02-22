def find(x,y):
    while x!=y:
        if x>y:
            x-=y
        else:
            y-=x
    return x
a1,a2,b1,b2=map(int,input().split())
a=a1*b2+a2*b1
b=a2*b2
c=find(a,b)
print(str(int(a/c))+"/"+str(int(b/c)))
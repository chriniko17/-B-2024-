def trans(x):
    return ord(x)-65
n=int(input())
for _ in range(n):
    a=[-2]*12
    for i in range(3):
        x,y,z=input().split()
        if z=="even":
            for j in range(len(x)):
                a[trans(x[j])],a[trans(y[j])]=0,0
        else:
            for j in range(12):
                if chr(j+65) not in set(x+y):
                    a[j]=0
            if z=="up":
                for j in range(len(x)):
                    if a[trans(x[j])]==-2:
                        a[trans(x[j])]=-1
                    elif a[trans(x[j])]==1:
                        a[trans(x[j])]=0
                    if a[trans(y[j])]==-2:
                        a[trans(y[j])]=1
                    elif a[trans(y[j])]==-1:
                        a[trans(y[j])]=0
            else:
                for j in range(len(x)):
                    if a[trans(x[j])]==-2:
                        a[trans(x[j])]=1
                    elif a[trans(x[j])]==-1:
                        a[trans(x[j])]=0
                    if a[trans(y[j])]==-2:
                        a[trans(y[j])]=-1
                    elif a[trans(y[j])]==1:
                        a[trans(y[j])]=0
        #print(a)
    for i in range(12):
        if a[i]==1:
            print(chr(i+65)+" is the counterfeit coin and it is light.")
            break
        elif a[i]==-1:
            print(chr(i+65)+" is the counterfeit coin and it is heavy.")
            break
n=int(input())
a=dict()
nm=[]
for i in range(n):
    name,size=input().split("-")
    if size[-1]=="M":
        num=float(size[0:len(size)-1])
    else:
        num=float(size[0:len(size)-1])*1000
    if name not in nm:
        nm.append(name)
        a[name]=[[size,num]]
    else:
        a[name].append([size,num])
nm.sort()
for name in nm:
    a[name].sort(key=lambda x:x[1])
    print(name+":",end=" ")
    for i in range(len(a[name])):
        print(a[name][i][0],end="")
        if i<len(a[name])-1:
            print(", ",end="")
    print()


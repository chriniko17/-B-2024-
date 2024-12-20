n=int(input())
a=[]
for i in range(n):
    a.append(input())
    a[i]=a[i][::-1]
for i in range(n):
    print(len(a[i])-a[i].count("0"))
    for j in range(len(a[i])):
        if a[i][j]!="0":
            #print(j,a[i][j])
            print(int(a[i][j])*(10**j),end=" ")
        else: continue
    print("")
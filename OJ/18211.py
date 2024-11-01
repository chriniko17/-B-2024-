p=int(input())
a=sorted(list(map(int,input().split())))
i,j=0,len(a)-1
we,op=0,0
if p<a[0]:
    print(0)
    exit()
while i<=j:
    while p>=a[i]:
        p-=a[i]
        i+=1
        we+=1
        if i==len(a):
            break
    #print(i+1,j+1)
    if we>op and i<j:
        p+=a[j]
        j-=1
        op+=1
    if i==j and p<a[i]:
        break
print(we-op)
n=int(input())
m=list(sorted(map(int,input().split()),reverse=True))
tot=sum(m)
o=0
#print(m,tot)
for i in range(n):
    o=o+m[i]
    if o>tot/2:
        print(i+1)
        exit()
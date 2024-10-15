a=input()
s=[0]*(len(a))
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        s[i]=s[i-1]+1
    else:
        s[i]=s[i-1]
#print(s)
m=int(input())
for _ in range(m):
    r,l=map(int,input().split())
    print(s[l-1]-s[r-1])
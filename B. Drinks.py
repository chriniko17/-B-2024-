n=int(input())
a=input()
num=[int(x) for x in a.split()]
ans=0
for i in range(n):
    ans=ans+num[i-1]
print(ans/n)
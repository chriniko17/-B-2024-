a=input()
ans=1
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        ans=ans+1
    else:
        ans=1
    if ans>= 7:
        print("YES")
        exit()
print("NO")
